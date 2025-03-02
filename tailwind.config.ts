import type { Config } from "tailwindcss";

const config = {
  darkMode: ["class"],
  content: [
    "./pages/**/*.{ts,tsx}",
    "./components/**/*.{ts,tsx}",
    "./app/**/*.{ts,tsx}",
    "./src/**/*.{ts,tsx}",
  ],
  prefix: "",
  theme: {
    container: {
      center: true,
      padding: "2rem",
      screens: {
        "2xl": "1400px",
      },
    },
    extend: {
      colors: {
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: {
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))",
        },
        secondary: {
          DEFAULT: "hsl(var(--secondary))",
          foreground: "hsl(var(--secondary-foreground))",
        },
        destructive: {
          DEFAULT: "hsl(var(--destructive))",
          foreground: "hsl(var(--destructive-foreground))",
        },
        muted: {
          DEFAULT: "hsl(var(--muted))",
          foreground: "hsl(var(--muted-foreground))",
        },
        accent: {
          DEFAULT: "hsl(var(--accent))",
          foreground: "hsl(var(--accent-foreground))",
        },
        popover: {
          DEFAULT: "hsl(var(--popover))",
          foreground: "hsl(var(--popover-foreground))",
        },
        card: {
          DEFAULT: "hsl(var(--card))",
          foreground: "hsl(var(--card-foreground))",
        },
      },
      dark: "selector",
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
      keyframes: {
        "accordion-down": {
          from: { height: "0" },
          to: { height: "var(--radix-accordion-content-height)" },
        },
        "accordion-up": {
          from: { height: "var(--radix-accordion-content-height)" },
          to: { height: "0" },
        },
      },
      animation: {
        "accordion-down": "accordion-down 0.2s ease-out",
        "accordion-up": "accordion-up 0.2s ease-out",
      },
      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
        "gradient-conic":
          "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
      },
      radialShape: {
        ellipse: "ellipse",
        circle: "circle",
      },
      radialSize: {
        "close-corner": "closest-corner",
        "close-side": "closest-side",
        "far-corner": "farthest-corner",
        "far-side": "farthest-side",
        "custom-size": (size: string) => size, // Allows custom sizes
      },
      radialPosition: {
        center: "at center",
        t: "at top",
        r: "at right",
        b: "at bottom",
        l: "at left",
        tr: "at top right",
        br: "at bottom right",
        bl: "at bottom left",
        tl: "at top left",
        custom: (position: string) => `at ${position}`, // Allows custom positions
      },
    },
  },
  plugins: [
    require("tailwindcss-animate"),
    require("tailwindcss/plugin")(function ({
      matchUtilities,
      theme,
    }: {
      matchUtilities: any;
      theme: any;
    }) {
      matchUtilities(
        {
          "bg-radial": (value: string) => {
        const [radialShape, radialSize, radialPosition] = value.split(" ");
        const shape = theme(`radialShape.${radialShape}`, radialShape);
        const size = theme(`radialSize.${radialSize}`, radialSize);
        const position = theme(`radialPosition.${radialPosition}`, radialPosition);
        return {
          "background-image": `radial-gradient(${shape} ${size} ${position}, var(--tw-gradient-stops))`,
        };
          },
        },
        {
          values: [
        config.theme.extend.radialShape,
        config.theme.extend.radialSize,
        config.theme.extend.radialPosition,
          ],
        }
      );
    }),
  ],
} satisfies Config;

export default config;
