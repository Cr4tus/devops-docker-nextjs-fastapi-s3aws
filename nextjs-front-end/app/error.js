'use client';

const Page = () => {
    return (
        <div className={style.container}>
            <h1 className={style.text}>{text.serverError}</h1>
        </div>
    );
};

const style = {
    container: 'w-full flex items-center justify-center',
    text: ''
};

const text = {
    serverError: 'Server Error Occurred.'
};

export default Page;