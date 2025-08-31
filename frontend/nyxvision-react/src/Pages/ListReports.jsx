 import axios from 'axios';
 import './ListReports.css';
 import React, { useEffect, useState } from "react";
 import formatDateString from '../Scripts/DateManipulations.js';
import NavBar from '../Componenets/NavBar.jsx';
 
 export default function ListReports(){
    const [reportData, setReportData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);;

    useEffect(() => {
        axios.get("http://localhost:8080/reports", {
            auth: {
                username: "kpperry",
                password: "password1212"
            }
        }).then( response => {
            setReportData(response.data);
            setLoading(false);
        })
        .catch((err) => {
            setError(err.message);
            setLoading(false);
        });

    }, []);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;

    let tableCategories = reportData.length > 0 ? Object.keys(reportData[0]) : [];

    return(
        <>
            <NavBar/>
            <div className="Reports">Reports</div>
            <div>
                
                <table className="reportTable">
                    <thead>
                        <tr>
                            <th>Report ID</th>
                            <th>Region</th>
                            <th>Threat Score</th>
                            <th>Summary</th>
                            <th>Classification</th>
                            <th>Source</th>
                            <th>Keywords</th>
                            <th>Uploaded</th>
                            <th>Time Processed</th>
                            <th>Details</th>
                        </tr>
                    </thead>
                    <tbody>
                        {reportData.map((row)=>(
                            <tr key={row.reportId}>
                                <td>{row.reportId}</td>
                                <td>{row.region}</td>
                                <td>{row.threatScore}</td>
                                <td>{row.summary}</td>
                                <td>{row.classification}</td>
                                <td>{row.source}</td>
                                <td>{row.keywords}</td>
                                <td>{formatDateString(row.timestamp)}</td>
                                <td>{formatDateString(row.processedDate)}</td>
                                <td>View more</td>
                            </tr>
                        ))}
                        </tbody>
                </table>
            </div>
        </>

    );
 }
