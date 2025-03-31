/** @type {import('next').NextConfig} */
const nextConfig = {
    output: 'standalone',
    images: {
        domains: ['cr4tus-qr-code-images.s3.amazonaws.com'],
    },
};

export default nextConfig;
