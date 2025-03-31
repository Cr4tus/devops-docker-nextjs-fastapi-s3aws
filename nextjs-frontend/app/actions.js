'use server';

import { redirect, RedirectType } from "next/navigation";
import { z } from "zod";

export const submitURL = async formData => {
    const userSubmittedURL = formData.get('url');

    const validationResultOfUserInput = z.string().url().safeParse(userSubmittedURL);
    if (!validationResultOfUserInput.success) {
        throw new Error(`Submitted an invalid URL: ${userSubmittedURL}`);
    }

    const response = await fetch(`http://localhost:8000/generate-qr/?url=${encodeURIComponent(validationResultOfUserInput.data)}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        }
    });
    
    if (!response.ok) {
        throw new Error(`Failed to generate the QR code for URL: ${userSubmittedURL}`);
    }
    
    const data = await response.json();
    
    redirect(`/?qrl=${data.qr_code_url}`, RedirectType.push);
};