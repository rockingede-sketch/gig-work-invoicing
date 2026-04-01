// import React from "react";

import {
  Box,
  Card,
  CardContent,
  TextField,
  Button,
  Typography,
  Divider,
  Link,
} from "@mui/material";
import { Link as RouterLink } from "react-router-dom";

export default function LoginPage() {
  return (
    <Box
      sx={{
        minHeight: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        px: 2,
        backgroundColor: "#f5f5f5",
      }}
    >
      <Card
        sx={{
          width: "100%",
          maxWidth: 420,
          boxShadow: 3,
          borderRadius: 2,
        }}
      >
        <CardContent sx={{ p: 4 }}>
          <Typography variant="h5" fontWeight={600} mb={2}>
            Kirjaudu
          </Typography>

          <TextField fullWidth label="Sähköposti" type="email" margin="normal" />

          <TextField fullWidth label="Salasana" type="password" margin="normal" />

          <Button fullWidth variant="contained" size="large" sx={{ mt: 2, py: 1.2 }}>
            Kirjaudu sisään
          </Button>

          <Box mt={2} textAlign="center">
            <Link component={RouterLink} to="/forgotPassword" underline="hover">
              Unohtunut salasana?
            </Link>
          </Box>

          <Divider sx={{ my: 3 }} />

          <Box textAlign="center">
            <Typography variant="body2" mb={1}>
              Eikö sinulla ole tiliä?
            </Typography>
            <Button component={RouterLink} to="/createAccount" variant="outlined" fullWidth>
              Luo tili
            </Button>
          </Box>
        </CardContent>
      </Card>
    </Box>
  );
}
