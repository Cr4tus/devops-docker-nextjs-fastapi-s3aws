import Form from "server-components/Form";
import QRCode from "server-components/QRCode";

const Page = async params => {
  const searchParams = await params.searchParams;
  
  return (
    <main className={style.container}>
      <QRCode sourceLink={searchParams.qrl} />
      <Form />
    </main>
  );
};

const style = {
  container: 'w-full py-20 flex flex-col flex-1 items-center justify-center gap-y-4'
};

export default Page;
