---
title: How to read a Reader twice
date: 2018-01-13
tags: 
    - dev
    - teereader
    - go
    - http
---

Some time ago I read about [`TeeReader`](https://golang.org/pkg/io/#TeeReader) but to be fair, I didn't give it that much thought. However, few month back I saw [a video](https://www.youtube.com/watch?v=c5ufcpTGIJM&list=PL64wiCrrxh4Jisi7OcCJIUpguV_f5jGnZ) by [@francesc](https://twitter.com/francesc) and his nice use case and I wrote down a new item in my mental TODO list about things I wanted to use.

Last week I had the chance to do it; we have a service that requires reading a request body to check for a `Status` field and also it requires to store the raw request.

What we were doing in the first iteration was unmarshalling the full payload into a struct and marshal the struct as the raw data. This process wasn't very reliable because it's pretty easy to lose information in during the un/marshalling.

To solve it we had two options:

1. Read all the body, store it in a variable and use that var as raw data and as an input to the `Unmarshal` call. Not very neat as you are not taking advantages of the [decoding streams](https://blog.golang.org/json-and-go#TOC_7.).
2. Use the `TeeReader`.

Here is an example (not with real names tho.) of what we end up doing:

```go
type Payload struct {
    Status int
}

func getStatusAndReason(r io.Reader) (string, string, error) {
        var buf bytes.Buffer
        tee := io.TeeReader(r, &buf)

        var payload Payload
        err := json.NewDecoder(tee).Decode(&payload)

        return payload.Status, buf.String(), err
}
```

I hope you liked our use case, and in case you would do in any other way, please, [do let me know](https://twitter.com/agonzalezro)! It's always nice learning from your experiences 😀
