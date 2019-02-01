This is a Flask app that demonstrates how to upload file(s) directly to S3 using pre-signed post.
The frontend is powered by Dropzone.js that enables features like drag-and-drop, queued upload, etc.
If you want to implement your uploader differently, please check the official Dropzone.js documentation and change the code accordingly.
The following is a sequence diagram that shows how requests bounce between different entities when a file is uploaded.
The primary advantages of this design are twofold.
* Upload can scale basically indefinitely, unlimited storage space and high concurrency support on S3.
* No need to expose AWS credentials to clients (browser, mobile app, etc.).
```
┌──────┐                       ┌──────┐          ┌──┐
│Client│                       │Server│          │S3│
└──┬───┘                       └──┬───┘          └┬─┘
   │   POST /get-presigned-post   │               │  
   │ ─────────────────────────────>               │  
   │                              │               │  
   │ RETURN S3 signed post in JSON│               │  
   │ <─────────────────────────────               │  
   │                              │               │  
   │     POST file to S3 URL with signed post     │  
   │ ─────────────────────────────────────────────>  
   │                              │               │  
   │            RETURN 200 confirmation           │  
   │ <─────────────────────────────────────────────  
┌──┴───┐                       ┌──┴───┐          ┌┴─┐
│Client│                       │Server│          │S3│
└──────┘                       └──────┘          └──┘

```

## Prerequisite

* Make sure the server running Flask app has sufficient IAM permissions to generate S3 pre-signed post.
* Make sure the destination bucket allows Cross-Origin Resource Sharing (CORS).
```xml
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
    <AllowedOrigin>*</AllowedOrigin>
    <AllowedMethod>PUT</AllowedMethod>
    <AllowedMethod>POST</AllowedMethod>
    <AllowedMethod>GET</AllowedMethod>
    <AllowedMethod>HEAD</AllowedMethod>
    <MaxAgeSeconds>3000</MaxAgeSeconds>
    <AllowedHeader>*</AllowedHeader>
</CORSRule>
</CORSConfiguration>
```

## Example

### Success
![success](./success.gif)

### Error
![error](./error.gif)

## Reference

* [https://www.dropzonejs.com/](https://www.dropzonejs.com/)
* [https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3.html](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3.html#generating-presigned-posts)
