import React from "react";
import Report from "./components/Report";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>PSh-Game Statistics Report</h1>
      </header>
      <main className="App-main">
        <Report />
      </main>
    </div>
  );
}

export default App;
