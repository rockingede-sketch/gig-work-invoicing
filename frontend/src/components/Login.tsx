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

export default function LoginPage() {
  return (
    <Box
      sx={{
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
        backgroundColor: "#f5f5f5",
      }}
    >
      {/* Top brand header */}
      <Box
        sx={{
          width: "100%",
          py: 3,
          backgroundColor: "#1a73e8", // Adjust to your brand color
          color: "white",
          textAlign: "center",
        }}
      >
        <Typography variant="h4" fontWeight={600}>
          Gig Billing System
        </Typography>
      </Box>

      {/* Centered login card */}
      <Box
        sx={{
          flexGrow: 1,
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          px: 2,
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
              Log in
            </Typography>

            <TextField fullWidth label="Email" type="email" margin="normal" />

            <TextField
              fullWidth
              label="Password"
              type="password"
              margin="normal"
            />

            <Button
              fullWidth
              variant="contained"
              size="large"
              sx={{ mt: 2, py: 1.2 }}
            >
              Log in
            </Button>

            <Box mt={2} textAlign="center">
              <Link href="#" underline="hover">
                Forgot your password?
              </Link>
            </Box>

            <Divider sx={{ my: 3 }} />

            <Box textAlign="center">
              <Typography variant="body2" mb={1}>
                Don’t have an account?
              </Typography>
              <Button variant="outlined" fullWidth>
                Create account
              </Button>
            </Box>
          </CardContent>
        </Card>
      </Box>
    </Box>
  );
}
