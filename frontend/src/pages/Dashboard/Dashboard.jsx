import { Typography, Box } from "@mui/material";

function Dashboard() {
  return (
    <Box sx={{ p: 4 }}>
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
  );
}

export default Dashboard;