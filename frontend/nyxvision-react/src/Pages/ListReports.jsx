 import axios from 'axios';
 import React, { useEffect, useState } from "react";
 
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
            <div>
                <table>
                    <thead>
                        <tr>
                            {tableCategories.map((value, i) => (
                                <th key={i}>{value}</th>
                            ))}
                        </tr>
                    </thead>
                    <tbody>
                        {reportData.map((report, rowIndex) => (
                            <tr key={rowIndex}>
                                {Object.values(report).map((val, colIndex) => (
                                <td key={colIndex}>
                                    {typeof val === "object" && val !== null
                                    ? JSON.stringify(val) 
                                    : val}
                                </td>
                                ))}
                            </tr>
                            ))}
                        </tbody>
                </table>
            </div>
        </>

    );
 }
