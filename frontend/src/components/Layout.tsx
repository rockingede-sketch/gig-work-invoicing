// src/components/Layout.tsx
import {
  AppBar,
  Toolbar,
  Typography,
  Box,
  Container,
  Button,
} from "@mui/material";
import { Outlet } from "react-router-dom";
import { Link } from "react-router-dom";

export default function Layout() {
  return (
    <Box sx={{ flexGrow: 1 }}>
      {/* HEADER */}
      <AppBar position="static" color="primary" elevation={1}>
        <Toolbar>
          <Typography variant="h6" sx={{ flexGrow: 1, textAlign: "left" }}>
            Keikkalasku
          </Typography>

          <Button color="inherit" component={Link} to="/">
            Etusivu
          </Button>
          <Button color="inherit" component={Link} to="/invoices">
            Laskutus
          </Button>
          <Button color="inherit" component={Link} to="/login">
            Kirjaudu
          </Button>
        </Toolbar>
      </AppBar>

      <Container sx={{ flex: 1, pt: 0, pb: 3 }}>
        {/* This is where child pages render */}
        <Outlet />
      </Container>
    </Box>
  );
}
