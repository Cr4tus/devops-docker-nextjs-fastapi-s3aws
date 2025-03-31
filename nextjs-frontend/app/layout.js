import "./globals.css";

export const metadata = {
  title: "QR Code Generator",
  description: "Generate QR codes for URLs form user",
};

const Layout = ({ children }) => {
  return (
    <html lang="en">
      <body>
        {children}
      </body>
    </html>
  );
};

export default Layout;
