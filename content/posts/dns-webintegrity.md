---
title: "WebIntegrity: a prototype for DNS-based website integrity"
tags:
- engineering
- web
- dns
- standards
---
RecipeRadar attempts to provide a transparent, reliable and trustworthy recipe search experience.  On this blog, we've previously written about a key aspect of that: our principle of using Open Source software whenever possible.

However, declaring that we use open source software does not, in itself, provide assurance of service integrity.  In particular: transparent and reassuring documentation about a named network communication service is a necessary prerequisite for trust, but users should also confirm that that they are indeed connected to that same named service -- and not some other intermediatry.

In communications security, a classic disruptive pattern that aims to subvert even the most honest service provider is the [Adversary-in-the-Middle attack](https://cwe.mitre.org/documents/glossary/index.html#Adversary-in-the-Middle).  When we send a letter to a friend, we would like to assume that they (and only they) receive it.  However, were someone else be able to intercept that message, then, in the absence of other protective measures, that intermediate person could create a subtly-adjusted forgery, and perhaps send that on to the intended recipient.

There are various ways to guard against this kind of disruption.  Two powerful techniques include: agreement of pre-shared authentication measures -- techniques that allow each partner to confirm that their messages are genuinely from each other, and that an adversary is unlikely to be aware of -- and the use of multiple channels of communication, so that an adversary would find it more difficult to intercept all of the relevant communications, something that they might need to do to keep their fabricated truth believable.

RecipeRadar provides service as part of the World Wide Web, one of the most (if not the most) open and democratic network environments that we are aware of.  On the web, service provision typically involves two key technologies: the Domain Name Service (DNS) protocol -- operated by Internet infrastructure providers -- and the [HyperText Transfer Protocol](https://datatracker.ietf.org/doc/html/rfc7231) (HTTP) -- operated by individual website owners.

Commonly-received wisdom on the web states that using Transport Layer Security (TLS) - sometimes anachronistically referred to as Secure Sockets Layer (SSL) - can provide integrity.  In brief: TLS is the feature that distinguishes plain-text HTTP communication from encrypted HTTPS communication: on the public web, TLS is implemented using public-key-based cryptography in combination with strict governance of the Certificate Authorities (CAs) who are able to mint trusted certificates.

It is true that TLS does provide integrity: if you are connected to a web service that uses TLS, then the messages sent to-and-fro can leverage the cryptographic properties of the communication channel to confirm, to a very high degree of probability, that messages have not been tampered with.  However, only you and the server are able to observe those communications, and so as an individual your recourse against individual servers that have obtained valid certificates through dubious means is limited.

Is there a way that we could achieve integrity for web users without relying upon secrecy?  We believe that there is - and we bootstrap our approach using an existing W3C standard called [SubResource Integrity](https://www.w3.org/TR/SRI/) (SRI).

SubResource Integrity allows a web browser -- an HTTP client -- to check whether the files (resources) mentioned on a webpage have the expected content if the browser chooses to download them.  To do this, the webpage must mention not only the filename, but it must also provide an `integrity` attribute that contains a checksum -- or multiple checksums -- corresponding to the expected content.

So, when your browser downloads the `index.html` page for RecipeRadar, we include the `integrity` HTML attribute on various subresources referenced in the page.  So far, so good; but how can you trust that you have received the intended `index.html` page?

Our solution is naive and limited, but is backwards and sideways compatible: we re-use the checksum format specified by W3C SRI, and place it into a DNS `B` TXT record.  At the time of writing, RecipeRadar returns the following responses from a DNS TXT query:

```
$ dig -t TXT reciperadar.com

; <<>> DiG 9.20.0-Debian <<>> -t TXT reciperadar.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 29630
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 2, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;reciperadar.com.               IN      TXT

;; ANSWER SECTION:
reciperadar.com.        3600    IN      TXT     "v=spf1 include:_spf.google.com ~all"
reciperadar.com.        3600    IN      TXT     "B=sha512-zq+vAQPEmB9RpcNiexq0+GLJqGsWim5jZskS1OtdnohK15D+UbQxGmKEeHQgEDiX1bK4c3CdygHdRlOlLEsGEQ== sha512-eRMiiXuO5gHP0byDCCxlc3KqA29H7SE+6y20/73cYEIiv7/m9ottwYm5GSbrjL6hhH9+JBPbD6s7a0rk3ZmSHA=="

;; AUTHORITY SECTION:
reciperadar.com.        3600    IN      NS      ns29.domaincontrol.com.
reciperadar.com.        3600    IN      NS      ns30.domaincontrol.com.

;; Query time: 36 msec
;; SERVER: 192.168.0.1#53(192.168.0.1) (UDP)
;; WHEN: Fri Aug 16 23:05:36 BST 2024
;; MSG SIZE  rcvd: 350
```

This communicates that an `HTTP GET /` -- a web request to the root path of an HTTP server -- to the `reciperadar.com` domain -- is expected to return content that matches one of the two SHA512 hash values included inthe `B` record.  Any other response content should be considered problematic by the HTTP client.

Publishing more than one active checksum means that we can deploy an updated version of our static web application while simultaneously allowing for the existing/stale version to remain valid.  When we become confident that clients reading current DNS results should receive fresh HTTP content, we can remove the outdated checksum.
