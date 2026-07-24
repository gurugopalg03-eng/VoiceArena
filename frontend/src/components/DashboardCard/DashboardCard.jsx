import { Card, CardContent, Typography } from "@mui/material";

function DashboardCard({ title, value }) {
  return (
    <Card
      elevation={3}
      sx={{
        minWidth: 250,
        borderRadius: 3,
      }}
    >
      <CardContent>
        <Typography
          variant="h6"
          color="text.secondary"
        >
          {title}
        </Typography>

        <Typography
          variant="h3"
          sx={{ mt: 2 }}
        >
          {value}
        </Typography>
      </CardContent>
    </Card>
  );
}

export default DashboardCard;
