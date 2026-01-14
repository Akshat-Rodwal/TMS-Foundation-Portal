import ImpactDashboard from "../components/ImpactDashboard";

function Home() {
    return (
        <>
            <header className="shell-header">
                <h1 className="shell-title">TMS Foundation Portal</h1>
                <p className="shell-subtitle">
                    Transparent impact overview for donors and stakeholders.
                </p>
            </header>
            <main className="shell-body">
                <ImpactDashboard />
            </main>
        </>
    );
}

export default Home;
