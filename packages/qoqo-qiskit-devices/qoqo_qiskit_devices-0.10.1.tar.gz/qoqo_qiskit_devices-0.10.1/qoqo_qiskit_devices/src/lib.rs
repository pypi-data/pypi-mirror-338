// Copyright © 2023-2025 HQS Quantum Simulations GmbH. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
// in compliance with the License. You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software distributed under the
// License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
// express or implied. See the License for the specific language governing permissions and
// limitations under the License.

//! # qoqo_qiskit_devices
//!
//! Qiskit devices' interface for qoqo.
//!
//! Collection of IBM's qiskit devices interfaces implementing qoqo's Device trait.

use pyo3::prelude::*;
use pyo3::types::PyDict;
use pyo3::wrap_pymodule;

pub mod devices;
pub use devices::*;

/// IBM python interface
///
/// Provides the devices that are used to execute quantum program on the IBM backend.
#[pymodule]
fn qoqo_qiskit_devices(_py: Python, module: &Bound<PyModule>) -> PyResult<()> {
    let wrapper = wrap_pymodule!(devices::ibm_devices);
    module.add_wrapped(wrapper)?;

    let system = PyModule::import(_py, "sys")?;
    let binding = system.getattr("modules")?;
    let system_modules: &Bound<PyDict> = binding.downcast()?;
    system_modules.set_item(
        "qoqo_qiskit_devices.devices",
        module.getattr("ibm_devices")?,
    )?;
    Ok(())
}
