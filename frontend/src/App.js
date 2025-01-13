import React from "react";
import Report from "./components/Report"; // Import the Report component
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>PSh-Game Statistics Report</h1>
      </header>
      <main>
        <Report /> {/* Include the Report component */}
      </main>
    </div>
  );
}

export default App;
