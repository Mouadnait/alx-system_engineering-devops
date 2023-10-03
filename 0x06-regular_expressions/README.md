# Alx School - 0x06.Regular expression 

Learn about regular expressions and building them using **Oniguruma** library which uses **Ruby** by default.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the `//`:

```
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
```

## Resource

<details>
<summary>Regular Expression</summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/mkcB0Yk1/image.png' border='0' alt='image'/></a>
<ul>
  <li>Links from screenshot
  <ul>
      <li><a href="https://www.regular-expressions.info/">regular-expressions</a></li>
      <li><a href="https://www.w3schools.com/jsref/jsref_obj_regexp.asp">Play with regexp</a></li>
      <li><a href="https://rubular.com/">Ruby</a></li>
      <li><a href="https://regex101.com/">PHP/Javascript/Python</a></li>
  </ul>
  </li>
</ul>
</details>

- [Regular expressions - basics](https://www.slideshare.net/neha_jain/introducing-regular-expressions)
- [Regular expressions - advanced](https://www.slideshare.net/neha_jain/advanced-regular-expressions-80296518)
- [Rubular is your best friend](https://rubular.com/)
- [Use a regular expression against a problem: now you have 2 problems](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/)
- [Learn Regular Expressions with simple, interactive exercises](https://regexone.com/)

## Tasks

<summary><a href="./0-simply_match_school.rb">0. Simply matching School</a></summary>

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/ec65557f0da1fbfbff6659413885e4d4822f5b1d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231003%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231003T125332Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5b2ea9649b1e422496b0fed8d771545afc8471ee577fc03bf5ce7bc16fcda831)

Requirements:

-   The regular expression must match `School`
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

Example:

```
sylvain@ubuntu$ ./0-simply_match_school.rb School | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_school.rb "Best School" | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_school.rb "School Best School" | cat -e
SchoolSchool$
sylvain@ubuntu$ ./0-simply_match_school.rb "Grace Hopper" | cat -e
$
```

<summary><a href="./1-repetition_token_0.rb">1. Repetition Token #0</a></summary>

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/e7db3c377d46453588fc84f3a975661d142fee91.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231003%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231003T125332Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2a40f6ce5162a4dc47cff0608d75a965fcd81594aa1986d40cb407981020e4d8)

Requirements:

-   Find the regular expression that will match the above cases
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

<summary><a href="./2-repetition_token_1.rb">2. Repetition Token #1</a></summary>

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/c59ff11db195d5cf17d1790a5141ae2f234786d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231003%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231003T125332Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1feeddc8005d151d51cf7de19a09ea6596bb66927ee351e50def06ed0fdbe6ef)

Requirements:

-   Find the regular expression that will match the above cases
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

<summary><a href="./3-repetition_token_2.rb">3. Repetition Token #2</a></summary>

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/3b6bf4aeca6a0c2de584e7f5d68d11eef57ce205.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231003%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231003T125332Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f19f609e024e42229b4631bec2a864f048f6626b3f50a74bbbdfbccdefb01afd)

Requirements:

-   Find the regular expression that will match the above cases
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

<summary><a href="./4-repetition_token_3.rb">4. Repetition Token #3</a></summary>

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/f8dbcb9cf5ae569a8645027dc46e81cb372ce28e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231003%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231003T125332Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=545a8599dffe03758d1d839dbd6e6566f080fd6b7eb09e4ab48866e27284ff7f)

Requirements:

-   Find the regular expression that will match the above cases
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
-   Your regex should not contain square brackets

<summary><a href="./5-beginning_and_end.rb">5. Not quite HBTN yet</a></summary>

Requirements:

-   The regular expression must be exactly matching a string that starts with h ends with n and can have any single character in between
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

Example:

```
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbn' | cat -e
hbn$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbtn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'h8n' | cat -e
h8n$
sylvain@ubuntu$
$
```

<summary><a href="./6-phone_number.rb">6. Call me maybe</a></summary>

This task is brought to you by a professional advisor Neha Jain, Senior Software Engineer at LinkedIn.

Requirement:

The regular expression must match a 10 digit phone number

Example:

```
sylvain@ubuntu$ ./6-phone_number.rb 4155049898 | cat -e
4155049898$
sylvain@ubuntu$ ./6-phone_number.rb " 4155049898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415 504 9898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415-504-9898" | cat -e
$
sylvain@ubuntu$
```

<summary><a href="./7-OMG_WHY_ARE_YOU_SHOUTING.rb">7. OMG WHY ARE YOU SHOUTING?</a></summary>

![](https://intranet.alxswe.com/images/contents/sysadmin/projects/78/shouting.jpg)

Requirement:

The regular expression must be only matching: capital letters

Example:

```
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e
ILOVESYSADMIN$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e
WHATSAY$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e
$
sylvain@ubuntu$
```

<details>
<summary><a href="./100-textme.rb">8. Textme</a></summary><br>
<a href='https://postimg.cc/3kzNT3Sb' target='_blank'><img src='https://i.postimg.cc/wBjmDvhH/image.png' border='0' alt='image'/></a>
<ul>
  <li>Links from screenshot
  <ul>
      <li><a href="./text_messages.log">text messages log file</a></li>
  </ul>
  </li>
</ul>
</details>