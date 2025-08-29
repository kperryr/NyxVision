import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import ListReports from "./Pages/ListReports";

function App() {

  return (
    <Router>
      <Routes>
        <Route path="/reports" element={<ListReports />} />
      </Routes>
    </Router>
  );
}

export default App;
