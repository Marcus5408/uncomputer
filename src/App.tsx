import { useState } from "react";
import reactLogo from "./assets/react.svg";
import { invoke } from "@tauri-apps/api/core";
import "./App.css";
import { Button } from "@/components/ui/button";

function App() {
  return (
    <div className="h-screen bg-black">
      <h1 className="pt-8 font-bold text-xl">UnComputer v0.1</h1>
      <Button>Click me</Button>
    </div>
  );
}

export default App;
