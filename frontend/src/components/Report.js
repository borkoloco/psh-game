import React, { useState, useEffect } from "react";
import axios from "axios";
import styled from "styled-components";

const ReportWrapper = styled.div`
  padding: 20px;
  font-family: Arial, sans-serif;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  margin-top: 20px;
`;

const Title = styled.h1`
  text-align: center;
  color: #4a90e2;
`;

const LastUpdated = styled.p`
  text-align: center;
  color: #888;
`;

const Button = styled.button`
  background-color: #4a90e2;
  color: white;
  padding: 12px 25px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  display: block;
  margin: 20px auto;
  font-size: 16px;

  &:hover {
    background-color: #357ab7;
  }
`;

const Table = styled.table`
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
  text-align: left;
`;

const TableHeader = styled.th`
  padding: 12px;
  background-color: #4a90e2;
  color: white;
`;

const TableCell = styled.td`
  padding: 12px;
  border: 1px solid #ddd;
`;

const TableRow = styled.tr`
  &:hover {
    background-color: #f9f9f9;
  }
`;

const PlayerImage = styled.img`
  width: 40px;
  height: 40px;
  border-radius: 50%;
`;
const Report = () => {
  const [stats, setStats] = useState([]);
  const [lastUpdated, setLastUpdated] = useState("");

  const fetchStats = async () => {
    try {
      const res = await axios.get(process.env.REACT_APP_API_URL);
      setStats(res.data.topPlayers);
      setLastUpdated(res.data.lastUpdated);
    } catch (error) {
      console.log("Error fetching stats:", error);
    }
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

  const handleImageError = (e) => {
    e.target.src = "https://randomuser.me/api/portraits/men/1.jpg";
  };

  return (
    <ReportWrapper>
      <Title>Top 10 Players</Title>
      <LastUpdated>Last updated: {lastUpdated}</LastUpdated>
      <Button onClick={exportCSV}>Export to CSV</Button>
      {stats.length === 0 ? (
        <p>No player data available at the moment.</p>
      ) : (
        <Table>
          <thead>
            <tr>
              <TableHeader>Player Image</TableHeader>
              <TableHeader>Player ID</TableHeader>
              <TableHeader>Nickname</TableHeader>
              <TableHeader>Score</TableHeader>
              <TableHeader>Creation Date</TableHeader>
            </tr>
          </thead>
          <tbody>
            {stats.map((stat) => (
              <TableRow key={stat.player_id}>
                <TableCell>
                  <PlayerImage
                    src={
                      stat.profile_image ||
                      "https://randomuser.me/api/portraits/men/1.jpg"
                    }
                    alt="Player Avatar"
                    onError={handleImageError}
                  />
                </TableCell>
                <TableCell>{stat.player_id}</TableCell>
                <TableCell>{stat.nickname}</TableCell>
                <TableCell>{stat.score}</TableCell>
                <TableCell>
                  {new Date(stat.creation_date).toLocaleString()}
                </TableCell>
              </TableRow>
            ))}
          </tbody>
        </Table>
      )}
    </ReportWrapper>
  );
};

export default Report;
