use std::collections::hash_map::Entry::{Occupied, Vacant};
use std::collections::HashMap;

use pyo3::prelude::*;
use pyo3::types::PyTuple;
use numpy::ToPyArray;

#[derive(Debug, Clone)]
pub struct Categorical {
    pub values: Vec<u32>,
    pub cats: HashMap<String, u32>,
    last: String,
    last_no: u32,
}

impl Categorical {
    pub fn new() -> Categorical {
        let xs = Vec::new();
        let hm = HashMap::new();
        Categorical {
            values: xs,
            cats: hm,
            last: "".to_string(),
            last_no: 0,
        }
    }

    pub fn new_empty(count: u32) -> Categorical {
        let mut res = Categorical::new();
        if count > 0 {
            res.cats.insert("".to_string(), 0);
            res.values.resize(count as usize, 0);
        }
        res
    }
    pub fn new_empty_push(count: u32, value: &str) -> Categorical {
        let mut res = Categorical::new_empty(count);
        res.push(value);
        res
    }

    pub fn push(&mut self, value: &str) {
        if value != self.last {
            // this little trick saves 2 allocations and about 2 seconds
            let next = self.cats.len() as u32;
            let no = match self.cats.entry(value.to_string()) {
                Vacant(entry) => entry.insert(next),
                Occupied(entry) => entry.into_mut(),
            };
            self.values.push(*no);
            self.last_no = *no;
            self.last = value.to_string();
        } else {
            self.values.push(self.last_no);
        }
    }

    pub fn len(&self) -> usize {
        self.values.len()
    }
}
impl<'py> IntoPyObject<'py> for Categorical {
    type Target = PyTuple; // the Python type
    type Output = Bound<'py, Self::Target>; // in most cases this will be `Bound`
    type Error = PyErr;

    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        // turn the cats into a vector instead of a dict
        // also means the must be continuous
        // but that's what pandas.Categorical wants
        let mut sorted: Vec<(&String, &u32)> = self.cats.iter().collect();
        sorted.sort_by(|a, b| a.1.cmp(b.1));
        let cats: Vec<String> = sorted.iter().map(|a| a.0.clone()).collect();
        //(self.values.into_object(py), cats.into_object(py)).into_object(py)
        (self.values.to_pyarray(py), cats.into_pyobject(py)?).into_pyobject(py)
    }
}
