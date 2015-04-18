About
=====

<script>
function getAge(dateString) {
    var today = new Date();
    var birthDate = new Date(dateString);
    var age = today.getFullYear() - birthDate.getFullYear();
    var m = today.getMonth() - birthDate.getMonth();
    if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }
    return age;
}
var age = getAge('4-4-1984');
</script>

My name is Alexandre González, I am a <script>document.write(age);</script> years
old Spanish developer currently working in UK, exactly in London at
[Shopa](http://www.shopa.com).

I came here in December 2012 to work from
[GreenManGaming](http://www.greenmangaming.com), I had a great time there but I
moved in October of 2014. I love travelling, so before working in London I was
doing it in Groningen, a beautiful place in Holland with my excolleagues of
[Paylogic](http://paylogic.nl).

![Photo of Alexandre González](../static/me.jpg)
<style>img{float: left; padding: 10px 15px 10px 0px;}</style>

My background is mainly technical, I studied Computer Science in Spain,
but at some point during my life I was interested in business too, so I
created my own company which was a complete economic disaster, but, I
learned a lot! At that time I studied a Master in Electronic Commerce too
because I thought that it could be useful. You should know too that I am
really passionate about FLOSS (Free as Libre Open Source Software).

Why?
----

The main reason of writing this blog is to improve my poor English and
talk about the things that I really love, that usually are related with
technology and specially with Python. You can see in the photo that I am
not lying about my passion :D If you want to take a photo like mine, you
can go to [Efteling](http://en.wikipedia.org/wiki/Efteling), I really
recommend it!

BTW, you can find the source code of this blog (generated with
[Polo](https://github.com/agonzalezro/polo)) at my [GitHub
profile](http://github.com/agonzalez/agonzalezro.github.io).
