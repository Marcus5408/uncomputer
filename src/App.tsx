import { useState } from "react";
import reactLogo from "./assets/react.svg";
import { invoke } from "@tauri-apps/api/core";
import "./App.css";
import { appWindow } from "@tauri-apps/plugin-window";

function App() {
  return (
    <>
      <p>hello world :3</p>
    </>
  );
}

export default App;
