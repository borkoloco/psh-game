// src/components/Report.js

import React, { useState, useEffect } from "react";
import axios from "axios";

const Report = () => {
  const [stats, setStats] = useState([]);
  const [lastUpdated, setLastUpdated] = useState("");

  const fetchStats = async () => {
    const res = await axios.get("http://localhost:8000/api/stats/");
    console.log(res.data);
    setStats(res.data.topPlayers);
    setLastUpdated(res.data.lastUpdated);
  };

  useEffect(() => {
    fetchStats();
    const interval = setInterval(fetchStats, 10000);
    return () => clearInterval(interval);
  }, []);

  const exportCSV = () => {
    const headers = ["Player ID", "Nickname", "Score", "Creation Date"];
    const rows = stats.map((stat) => [
      stat.player_id,
      stat.nickname,
      stat.score,
      stat.creation_date,
    ]);

    const csvContent = [
      headers.join(","),
      ...rows.map((row) => row.join(",")),
    ].join("\n");

    const blob = new Blob([csvContent], { type: "text/csv" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "report.csv";
    link.click();
  };

  return (
    <div>
      <h1>Top 10 Players</h1>
      <p>Last updated: {lastUpdated}</p>
      <button onClick={exportCSV}>Export to CSV</button>
      <table>
        <thead>
          <tr>
            <th>Player ID</th>
            <th>Nickname</th>
            <th>Score</th>
            <th>Creation Date</th>
          </tr>
        </thead>
        <tbody>
          {stats.map((stat) => (
            <tr key={stat.player_id}>
              <td>{stat.player_id}</td>
              <td>{stat.nickname}</td>
              <td>{stat.score}</td>
              <td>{new Date(stat.creation_date).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Report;
