import { Box, Grid } from "@mui/material";
import Header from "../../components/Header/Header";
import Sidebar from "../../components/Sidebar/Sidebar";
import DashboardCard from "../../components/DashboardCard/DashboardCard";

function Dashboard() {
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
                value="0"
              />
            </Grid>

            <Grid size={{ xs: 12, md: 6, lg: 3 }}>
              <DashboardCard
                title="Competitions"
                value="0"
              />
            </Grid>

            <Grid size={{ xs: 12, md: 6, lg: 3 }}>
              <DashboardCard
                title="Organizations"
                value="0"
              />
            </Grid>

            <Grid size={{ xs: 12, md: 6, lg: 3 }}>
              <DashboardCard
                title="Users"
                value="0"
              />
            </Grid>
          </Grid>
        </Box>
      </Box>
    </>
  );
}

export default Dashboard;
