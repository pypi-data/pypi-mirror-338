
use pyo3::prelude::*;
use pyo3::types::{PyModule};


mod rutrun;


/// A Python module for security protections in Chile
/// 
/// Chilenian specific security protection options like rut/run
#[pymodule]
pub fn cl(py: Python, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(rutrun::rut_run_checker, m)?)?;
    m.add("ValidationError", py.get_type::<rutrun::ValidationError>())?;
    Ok(())
}