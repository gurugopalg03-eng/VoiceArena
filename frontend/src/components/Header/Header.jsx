import {
  AppBar,
  Toolbar,
  Typography,
  Button,
  Box,
} from "@mui/material";

function Header() {
  const email = localStorage.getItem("email");

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("email");
    window.location.href = "/";
  };

  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6">
          🎙 VoiceArena
        </Typography>

        <Box sx={{ flexGrow: 1 }} />

        <Typography sx={{ mr: 3 }}>
          Welcome {email}
        </Typography>

        <Button
          color="inherit"
          onClick={handleLogout}
        >
          LOGOUT
        </Button>
      </Toolbar>
    </AppBar>
  );
}

export default Header;