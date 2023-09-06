"use client";

import { createContext, useContext, useState } from "react";

type AuthContextType = {
  authToken: string;
  setAuthToken: (token: string) => void;
  handleLogout: () => void;
};

export const AuthContext = createContext<AuthContextType | undefined>(
  undefined
);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [authToken, setAuthToken] = useState<string>("");

  function handleAuthToken(token: string) {
    setAuthToken(token);
  }

  function handleLogout() {
    setAuthToken("");
  }

  const value = {
    authToken,
    setAuthToken: handleAuthToken,
    handleLogout,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}
