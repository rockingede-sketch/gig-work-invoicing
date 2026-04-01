import { useState } from "react";
import {
  Box,
  Button,
  Stepper,
  Step,
  StepLabel,
  Paper,
  Typography,
} from "@mui/material";

import {
  type PersonalInfo,
  type BankTaxInfo,
  type ProfileData,
} from "../../../types/profile";

import { type PersonalInfoStep } from "./PersonalInfoStep";
import { type BankTaxInfoStep } from "./BankTaxInfoStep";

const steps = ["Personal Info", "Bank & Tax Info"];

const initialPersonal: PersonalInfo = {
  firstName: "",
  lastName: "",
  email: "",
};

const initialBankTax: BankTaxInfo = {
  iban: "",
  bic: "",
  taxId: "",
  vatNumber: "",
};

export function ProfileOnboarding() {
  const [activeStep, setActiveStep] = useState(0);
  const [personal, setPersonal] = useState(initialPersonal);
  const [bankTax, setBankTax] = useState(initialBankTax);
  const [submitted, setSubmitted] = useState(false);

  const isLastStep = activeStep === steps.length - 1;

  const handleNext = () => {
    if (isLastStep) {
      const payload: ProfileData = { ...personal, ...bankTax };
      console.log("Submit to API:", payload);
      setSubmitted(true);
    } else {
      setActiveStep((prev) => prev + 1);
    }
  };

  const handleBack = () => setActiveStep((prev) => prev - 1);

  const renderStep = () => {
    switch (activeStep) {
      case 0:
        return (
          <PersonalInfoStep
            values={personal}
            onChange={(field, value) =>
              setPersonal((prev) => ({ ...prev, [field]: value }))
            }
          />
        );
      case 1:
        return (
          <BankTaxInfoStep
            values={bankTax}
            onChange={(field, value) =>
              setBankTax((prev) => ({ ...prev, [field]: value }))
            }
          />
        );
      default:
        return null;
    }
  };

  if (submitted) {
    return (
      <Paper sx={{ p: 4, maxWidth: 600, mx: "auto", mt: 6 }}>
        <Typography variant="h5">Profile Completed</Typography>
        <Typography>You can now access your dashboard.</Typography>
      </Paper>
    );
  }

  return (
    <Paper sx={{ p: 4, maxWidth: 600, mx: "auto", mt: 6 }}>
      <Typography variant="h5" gutterBottom>
        Complete Your Profile
      </Typography>

      <Stepper activeStep={activeStep} sx={{ my: 3 }}>
        {steps.map((label) => (
          <Step key={label}>
            <StepLabel>{label}</StepLabel>
          </Step>
        ))}
      </Stepper>

      {renderStep()}

      <Box display="flex" justifyContent="space-between" mt={4}>
        <Button
          variant="outlined"
          disabled={activeStep === 0}
          onClick={handleBack}
        >
          Back
        </Button>

        <Button variant="contained" onClick={handleNext}>
          {isLastStep ? "Finish" : "Next"}
        </Button>
      </Box>
    </Paper>
  );
}
