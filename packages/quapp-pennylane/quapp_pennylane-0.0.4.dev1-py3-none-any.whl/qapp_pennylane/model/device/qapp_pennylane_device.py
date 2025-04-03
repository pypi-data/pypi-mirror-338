"""
    QApp Platform Project
    qapp_pennylane_device.py
    Copyright © CITYNOW Co. Ltd. All rights reserved.
"""
import math
import time

import pennylane as qml
from pennylane.tape import QuantumTape
from qapp_common.config.logging_config import logger
from qapp_common.data.device.circuit_running_option import CircuitRunningOption
from qapp_common.data.response.authentication import Authentication
from qapp_common.data.response.project_header import ProjectHeader
from qapp_common.enum.invocation_step import InvocationStep
from qapp_common.model.device.custom_device import CustomDevice
from qapp_common.model.provider.provider import Provider


class QAppPennylaneDevice(CustomDevice):
    def __init__(self, provider: Provider, device_specification: str):
        super().__init__(provider, device_specification)
        logger.debug('[QAppPennylaneDevice] Initializing device specification')
        self.device_specification = device_specification

    def _create_job(self, circuit, options: CircuitRunningOption):
        """
        @param circuit: circuit to run
        @param options: options for running circuit
        ex: options.shots: number of shots
        
        run the circuit and return the result
        """
        logger.debug(
            '[QAppPennylaneDevice] Creating job with {0} shots'.format(
                options.shots))

        with QuantumTape() as tape:
            circuit()

        parts = self.device_specification.split('/')
        device_name = parts[0]

        """
        with rigetti device, device_specification includes 
        rigetti.qvm/9q-square-pyqvm, 9q-square-qvm: 9qubit
        rigetti.qvm/Nq-pyqvm, Nq-qvm: Nqubit (32 with QApp platform)
        """
        unsupported_default_qubit_autograd = qml.__version__ > '0.37.0' and device_name == 'default.qubit.autograd'
        if not qml.plugin_devices.__contains__(device_name):
            if unsupported_default_qubit_autograd:
                logger.warning(
                    f'[QAppPennylaneDevice] Using default.qubit for device {device_name} in PennyLane version {qml.__version__}')
            else:
                logger.error(
                    f'[QAppPennylaneDevice] The device {device_name} is not supported in PennyLane version {qml.__version__}.')
                raise ValueError(
                    f'The device {device_name} is not supported in PennyLane version {qml.__version__}. '
                )

        if device_name == "rigetti.qvm":
            device_type = parts[1]
            if parts[1] in ["9q-square-qvm", "9q-square-pyqvm"]:
                self.device = qml.device(device_name, device=device_type,
                                         shots=options.shots)
            else:
                self.device = qml.device(device_name, device=str(tape.num_wires) + device_type[1:],
                                         shots=options.shots)
        elif unsupported_default_qubit_autograd:
            self.device = qml.device('default.qubit', wires=tape.wires, shots=options.shots)
        else:
            self.device = qml.device(device_name, wires=tape.wires, shots=options.shots)

        start_time = time.time()

        qnode_params = {'interface': "autograd",
                        'diff_method': "parameter-shift"} if unsupported_default_qubit_autograd else {}
        qnode = qml.QNode(circuit, self.device, **qnode_params)

        job_result = qnode()
        end_time = time.time()

        result_histogram = {}

        # generate histogram
        if qml.probs() in qnode.tape.observables:
            histogram_index = qnode.tape.observables.index(qml.probs())
            probs = job_result[histogram_index]
            num_bits = math.ceil(math.log2(len(probs)))
            for i, prob in enumerate(probs):
                bitstring = format(i, f'0{num_bits}b')
                result_histogram[bitstring] = int(prob * options.shots)
        else:
            result_histogram = None

        shots = getattr(qnode.device, 'shots', options.shots)

        data = {"result": job_result, "histogram": result_histogram,
                "time_taken_execute": end_time - start_time, "shots": shots}

        logger.info(data)
        return data

    def _is_simulator(self) -> bool:
        logger.debug('[QAppPennylaneDevice] Is simulator')
        return True

    def _produce_histogram_data(self, job_result) -> dict | None:
        logger.info('[PennylaneDevice] Producing histogram data')

        histogram = job_result.get('histogram')

        if histogram is None:
            logger.debug("[PennylaneDevice] Can't produce histogram")

        return job_result.get('histogram')

    def _get_provider_job_id(self, job) -> str:
        logger.debug('[PennylaneDevice] Getting job id')

        # no job id in local simulator
        return ""

    def _get_job_status(self, job) -> str:
        logger.debug('[PennylaneDevice] Getting job status')

        return "DONE"

    def _get_job_result(self, job) -> dict:
        logger.debug('[PennylaneDevice] Getting job result')

        return job

    def _calculate_execution_time(self, job_result):
        logger.debug('[PennylaneDevice] Calculating execution time')

        self.execution_time = job_result.get('time_taken_execute')

        logger.debug(
            '[PennylaneDevice] Execution time calculation was: {0} seconds'.format(
                self.execution_time))

    def run_circuit(self,
                    circuit,
                    post_processing_fn,
                    options: CircuitRunningOption,
                    callback_dict: dict,
                    authentication: Authentication,
                    project_header: ProjectHeader):
        """
        @param project_header: project header
        @param callback_dict: callback url dictionary
        @param options: Options for run circuit
        @param authentication: Authentication for calling quao server
        @param post_processing_fn: Post-processing function
        @param circuit: Circuit was run
        """
        original_job_result, job_response = self._on_execution(
            authentication=authentication,
            project_header=project_header,
            execution_callback=callback_dict.get(InvocationStep.EXECUTION),
            circuit=circuit,
            options=options)

        if original_job_result is None:
            return

        job_response = self._on_analysis(
            job_response=job_response,
            original_job_result=original_job_result,
            analysis_callback=callback_dict.get(InvocationStep.ANALYSIS))

        if job_response is None:
            return

        self._on_finalization(job_result=original_job_result.get('result'),
                              authentication=authentication,
                              post_processing_fn=post_processing_fn,
                              finalization_callback=callback_dict.get(
                                  InvocationStep.FINALIZATION),
                              project_header=project_header)

    def _get_shots(self, job_result) -> int | None:
        """
        Retrieve the number of shots from the job result.

        This method checks if the job result contains the 'shots' attribute
        and returns its value. If the 'shots' attribute is not present,
        the method returns None.

        Args:
            job_result: An object representing the result of a job, which
                        may contain the number of shots.

        Returns:
            int | None: The number of shots if available; otherwise, None.
        """
        logger.debug('[PennylaneDevice] Calculating number of shots')

        return getattr(job_result, 'shots', None)
