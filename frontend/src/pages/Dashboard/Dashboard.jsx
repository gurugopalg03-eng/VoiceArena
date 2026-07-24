import { Box, Typography } from "@mui/material";
import Header from "../../components/Header/Header";
import Sidebar from "../../components/Sidebar/Sidebar";

function Dashboard() {
  return (
    <>
      <Header />

      <Box sx={{ display: "flex" }}>
        <Sidebar />

        <Box sx={{ flexGrow: 1, p: 4 }}>
          <Typography variant="h3" gutterBottom>
            🎙 VoiceArena Dashboard
          </Typography>

          <Typography variant="h6">
            Welcome to VoiceArena!
          </Typography>

          <Typography sx={{ mt: 2 }}>
            Login Successful ✅
          </Typography>
        </Box>
      </Box>
    </>
  );
}

export default Dashboard;