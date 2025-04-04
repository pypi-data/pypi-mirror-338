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

//! # roqoqo_qiskit_devices
//!
//! Qiskit devices' interface for roqoqo.
//!
//! Collection of IBM's qiskit devices interfaces implementing roqoqo's Device trait.

#[allow(deprecated)]
pub mod devices;
pub use devices::{
    IBMBelemDevice, IBMDevice, IBMJakartaDevice, IBMLagosDevice, IBMLimaDevice, IBMManilaDevice,
    IBMNairobiDevice, IBMPerthDevice, IBMQuitoDevice,
};
