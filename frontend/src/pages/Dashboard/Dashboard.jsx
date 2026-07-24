import { useEffect, useState } from "react";
import { Box, Grid } from "@mui/material";
import Header from "../../components/Header/Header";
import Sidebar from "../../components/Sidebar/Sidebar";
import DashboardCard from "../../components/DashboardCard/DashboardCard";
import { getDashboardSummary } from "../../services/dashboardService";

function Dashboard() {
  const [summary, setSummary] = useState({
    participants: 0,
    competitions: 0,
    organizations: 0,
    users: 0,
  });

  useEffect(() => {
    loadDashboard();
  }, []);

  const loadDashboard = async () => {
    try {
      const data = await getDashboardSummary();
      setSummary(data);
    } catch (error) {
      console.error("Failed to load dashboard:", error);
    }
  };

  return (
    <>
      <Header />

      <Box sx={{ display: "flex" }}>
        <Sidebar />

        <Box sx={{ flexGrow: 1, p: 4 }}>
          <Grid container spacing={3}>
            <Grid size={{ xs: 12, md: 6, lg: 3 }}>
              <DashboardCard
                title="Participants"
                value={summary.participants}
              />
            </Grid>

            <Grid size={{ xs: 12, md: 6, lg: 3 }}>
              <DashboardCard
                title="Competitions"
                value={summary.competitions}
              />
            </Grid>

            <Grid size={{ xs: 12, md: 6, lg: 3 }}>
              <DashboardCard
                title="Organizations"
                value={summary.organizations}
              />
            </Grid>

            <Grid size={{ xs: 12, md: 6, lg: 3 }}>
              <DashboardCard
                title="Users"
                value={summary.users}
              />
            </Grid>
          </Grid>
        </Box>
      </Box>
    </>
  );
}

export default Dashboard;