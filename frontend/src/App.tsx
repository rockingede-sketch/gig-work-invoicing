import Layout from "./components/Layout";
import LoginPage from "./features/auth/components/LoginPage";
import ForgotPassword from "./features/auth/components/ForgotPassword";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from "./app/routes/Homepage";
import CreateAccount from "./features/auth/components/CreateAccount";

import "./App.css";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />}>
          <Route path="/" element={<HomePage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/forgotPassword" element={<ForgotPassword />} />
          <Route path="/createAccount" element={<CreateAccount />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

// import { CssBaseline, ThemeProvider, createTheme, Box } from "@mui/material";
// import { ProfileOnboarding } from "./components/onboarding/ProfileOnboarding";

// const theme = createTheme();

// function App() {
//   return (
//     <ThemeProvider theme={theme}>
//       <CssBaseline />
//       <Box minHeight="100vh" bgcolor="#f5f5f5">
//         <ProfileOnboarding />
//       </Box>
//     </ThemeProvider>
//   );
// }

// export default App;
