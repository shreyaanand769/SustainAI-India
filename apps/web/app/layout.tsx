import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'BharatSustain AI | Adaptive Sustainability OS',
  description: "India's multi-agent climate, infrastructure, and policy intelligence platform."
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
