// Switcher interactif de Palettes pour L'OCHJU
// Permet de tester en direct dans le navigateur les Palettes 1, 3 et 5 sans recharger

const PALETTES = {
  // Palette 1 : Granit de l'Alta Rocca & Or Électrique
  palette1: {
    id: "palette1",
    name: "Palette 1 : Granit & Or Électrique",
    bgBody: "#121316",
    bgCard: "#1a1c22",
    bgSurface: "#22252c",
    borderCard: "#2e323b",
    borderSubtle: "#242730",
    textPrimary: "#f8fafc",
    textSecondary: "#cbd5e1",
    textMuted: "#94a3b8",
    goldMain: "#fbbf24",
    goldMuted: "#f59e0b",
    accentRed: "#ef4444",
    gridOpacity: "0.06",
    glowColor: "rgba(251, 191, 36, 0.18)"
  },

  // Palette 3 : Noir Monochromatique & Or Pur 24K
  palette3: {
    id: "palette3",
    name: "Palette 3 : Noir Absolu & Or 24K",
    bgBody: "#000000",
    bgCard: "#0a0a0a",
    bgSurface: "#121212",
    borderCard: "#222222",
    borderSubtle: "#181818",
    textPrimary: "#ffffff",
    textSecondary: "#e5e5e5",
    textMuted: "#888888",
    goldMain: "#ffd700",
    goldMuted: "#e5b700",
    accentRed: "#dc2626",
    gridOpacity: "0.03",
    glowColor: "rgba(255, 215, 0, 0.22)"
  },

  // Palette 5 : Nébuleuse Émeraude Maquis & Or Impérial
  palette5: {
    id: "palette5",
    name: "Palette 5 : Émeraude Maquis & Or",
    bgBody: "#060d09",
    bgCard: "#0b1711",
    bgSurface: "#12241b",
    borderCard: "#1b3628",
    borderSubtle: "#14281e",
    textPrimary: "#f0fdf4",
    textSecondary: "#dcfce7",
    textMuted: "#86efac",
    goldMain: "#f59e0b",
    goldMuted: "#d97706",
    accentRed: "#f97316",
    gridOpacity: "0.05",
    glowColor: "rgba(245, 158, 11, 0.16)"
  }
};

export default PALETTES;
