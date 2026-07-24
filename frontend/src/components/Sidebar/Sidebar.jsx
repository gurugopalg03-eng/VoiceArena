import { Box, List, ListItemButton, ListItemText } from "@mui/material";

function Sidebar() {
  return (
    <Box
      sx={{
        width: 240,
        height: "100vh",
        borderRight: "1px solid #ddd",
        bgcolor: "#fafafa",
      }}
    >
      <List>
        <ListItemButton>
          <ListItemText primary="🏠 Dashboard" />
        </ListItemButton>

        <ListItemButton>
          <ListItemText primary="👤 Participants" />
        </ListItemButton>

        <ListItemButton>
          <ListItemText primary="🏆 Competitions" />
        </ListItemButton>

        <ListItemButton>
          <ListItemText primary="🏢 Organizations" />
        </ListItemButton>

        <ListItemButton>
          <ListItemText primary="👥 Users" />
        </ListItemButton>
      </List>
    </Box>
  );
}

export default Sidebar;