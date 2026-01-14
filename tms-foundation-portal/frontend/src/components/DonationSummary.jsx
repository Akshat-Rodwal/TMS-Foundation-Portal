function DonationSummary({ totalAmount, donationCount, activePrograms }) {
    return (
        <div className="metrics-grid">
            <div className="metric-card">
                <div className="metric-label">Total Donations</div>
                <div className="metric-value">₹{totalAmount}</div>
                <div className="metric-caption">
                    Combined support received across all active programs.
                </div>
            </div>
            <div className="metric-card">
                <div className="metric-label">Number of Donations</div>
                <div className="metric-value">{donationCount}</div>
                <div className="metric-caption">
                    Individual contributions recorded in the current dataset.
                </div>
            </div>
            <div className="metric-card">
                <div className="metric-label">Active Programs</div>
                <div className="metric-value">{activePrograms}</div>
                <div className="metric-caption">
                    Ongoing initiatives currently serving communities.
                </div>
            </div>
        </div>
    );
}

export default DonationSummary;
