import { z } from "zod";
import Image from "next/image";

const QRCode = ({ sourceLink }) => {
    if (!sourceLink || !z.string().url().safeParse(sourceLink).success) {
        return null;
    }

    return (
        <div className={style.container}>
            <h1 className={style.title}>{text.title}</h1>
            <h2 className={style.url}>{`${sourceLink.split('/').pop().replace(/\.png$/, "")}`}</h2>
            <Image src={sourceLink} alt="QR Code" className={style.image} width={200} height={200} />
        </div>
    );
};

const style = {
    container: 'w-full flex flex-1 flex-col items-center justify-center',
    title: 'text-xl',
    url: 'text-blue-400',
    image: 'mt-12 rounded-xl'
};

const text = {
    title: 'Scan QR for:'
};

export default QRCode;