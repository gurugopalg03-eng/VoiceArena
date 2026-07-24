import { useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  Box,
  Button,
  Card,
  CardContent,
  Container,
  TextField,
  Typography,
} from "@mui/material";
import { login } from "../../services/authService";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      const data = await login(email, password);

      localStorage.setItem("token", data.access_token);

      alert("Login Successful!");

      navigate("/dashboard");
    } catch (error) {
      console.error(error);
      alert("Invalid Email or Password");
    }
  };

  return (
    <Box
      sx={{
        minHeight: "100vh",
        backgroundColor: "#f5f7fa",
        display: "flex",
        alignItems: "center",
      }}
    >
      <Container maxWidth="sm">
        <Card elevation={8}>
          <CardContent sx={{ p: 5 }}>
            <Typography
              variant="h3"
              align="center"
              gutterBottom
              color="primary"
            >
              🎙 VoiceArena
            </Typography>

            <Typography
              variant="body1"
              align="center"
              color="text.secondary"
              sx={{ mb: 4 }}
            >
              Sign in to continue
            </Typography>

            <TextField
              fullWidth
              label="Email"
              margin="normal"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />

            <TextField
              fullWidth
              type="password"
              label="Password"
              margin="normal"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />

            <Button
              variant="contained"
              fullWidth
              size="large"
              sx={{ mt: 3 }}
              onClick={handleLogin}
            >
              LOGIN
            </Button>
          </CardContent>
        </Card>
      </Container>
    </Box>
  );
}

export default Login;