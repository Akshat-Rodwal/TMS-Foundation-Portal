import { useEffect, useState } from "react";
import apiClient from "../api/apiClient";
import DonationSummary from "./DonationSummary";

function ImpactDashboard() {
    const [summary, setSummary] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    useEffect(() => {
        async function loadSummary() {
            try {
                const response = await apiClient.get("impact/summary/");
                setSummary(response.data);
            } catch (err) {
                setError("Unable to load impact data.");
            } finally {
                setLoading(false);
            }
        }

        loadSummary();
    }, []);

    if (loading) {
        return <section className="loading">Loading impact data...</section>;
    }

    if (error) {
        return <section className="error">{error}</section>;
    }

    return (
        <section>
            <div
                style={{
                    display: "flex",
                    justifyContent: "space-between",
                    alignItems: "center",
                    marginBottom: 16,
                }}
            >
                <h2 className="section-title">Impact Dashboard</h2>
                <div className="status-pill">
                    <span className="status-dot" />
                    Live data from backend
                </div>
            </div>
            {summary && (
                <>
                    <DonationSummary
                        totalAmount={summary.total_amount}
                        donationCount={summary.donation_count}
                        activePrograms={summary.active_programs}
                    />
                    <p className="helper-text">
                        This snapshot reflects the current{" "}
                        <span className="helper-highlight">donor support</span>{" "}
                        and{" "}
                        <span className="helper-highlight">
                            active programs
                        </span>{" "}
                        across TMS Foundation initiatives.
                    </p>
                </>
            )}
        </section>
    );
}

export default ImpactDashboard;
