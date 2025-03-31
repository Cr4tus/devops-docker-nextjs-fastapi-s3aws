import { submitURL } from "@/app/actions";

const Form = () => {
    return (
        <form action={submitURL} className={style.container}>
            <input
                type="text"
                name="url"
                required={true}
                autoFocus={true}
                placeholder={text.urlPlaceholder}
                className={style.urlInput}
            />
            <button type="submit" className={style.submitButton}>{text.generateQRCode}</button>
        </form>
    );
};

const style = {
    container: 'px-2 py-2 flex gap-x-2 items-center border-solid border-white border-[2px] rounded-xl lg:min-w-[48rem]',
    urlInput: 'flex flex-1 rounded-lg focus:outline-none focus:ring-0 focus:border-transparent',
    submitButton: 'px-2 py-1 bg-blue-500 rounded-lg hover:bg-transparent hover:text-blue-500'
};

const text = {
    urlPlaceholder: 'Enter an URL like https://example.com',
    generateQRCode: 'Generate QR Code'
};

export default Form;