# termux-packages
Android terminal and Linux environment - Solve the installation problem packages repository.
# How to use
<p>Run <code>apt edit-sources</code>, comment out existing URLs and add line for picked mirror, or use the <code>termux-change-repo</code> script that is part of the <code>termux-tools</code> package.</p>
<h2>
<a id="user-content-mirrors-by-a1batross" class="anchor" href="#mirrors-by-a1batross" aria-hidden="true"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"></svg></a>Mirrors by <a href="https://github.com/a1batross">a1batross</a>
</h2>
<p>Updated once per 6 hours.</p>
<table role="table">
<thead>
<tr>
<th align="left">Repository</th>
<th align="left">sources.list entry</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><a href="https://github.com/termux/termux-packages">Main</a></td>
<td align="left"><code>deb https://termux.mentality.rip/termux-packages-24 stable main</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/game-packages">Games</a></td>
<td align="left"><code>deb https://termux.mentality.rip/game-packages-24 games stable</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/termux-root-packages">Root</a></td>
<td align="left"><code>deb https://termux.mentality.rip/termux-root-packages-24 root stable</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/science-packages">Science</a></td>
<td align="left"><code>deb https://termux.mentality.rip/science-packages-24 science stable</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/unstable-packages">Unstable</a></td>
<td align="left"><code>deb https://termux.mentality.rip/unstable-packages unstable main</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/x11-packages">X11</a></td>
<td align="left"><code>deb https://termux.mentality.rip/x11-packages x11 main</code></td>
</tr>
</tbody>
</table>
<h2>
<a id="user-content-mirrors-by-grimler" class="anchor" href="#mirrors-by-grimler" aria-hidden="true"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"></svg></a>Mirrors by <a href="https://github.com/grimler91">Grimler</a>
</h2>
<p>Mirrors for termux-packages, game-packages, science-packages and termux-root-packages are updated directly from github actions. x11-packages and unstable-packages are mirrored and synchronized manually for now.</p>
<table role="table">
<thead>
<tr>
<th align="left">Repository</th>
<th align="left">sources.list entry</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><a href="https://github.com/termux/termux-packages">Main</a></td>
<td align="left"><code>deb https://grimler.se/termux-packages-24 stable main</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/game-packages">Games</a></td>
<td align="left"><code>deb https://grimler.se/game-packages-24 games stable</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/termux-root-packages">Root</a></td>
<td align="left"><code>deb https://grimler.se/termux-root-packages-24 root stable</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/science-packages">Science</a></td>
<td align="left"><code>deb https://grimler.se/science-packages-24 science stable</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/unstable-packages">Unstable</a></td>
<td align="left"><code>deb https://grimler.se/unstable-packages unstable main</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/x11-packages">X11</a></td>
<td align="left"><code>deb https://grimler.se/x11-packages x11 main</code></td>
</tr>
</tbody>
</table>
  
  
#Modify <code> /files/usr/etc/apt/sources.list </code> as follows 2021
<table role="table">
<thead>
<tr>
<th align="left">Repository</th>
<th align="left">sources.list entry</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><a href="https://github.com/termux/termux-packages">Main</a></td>
<td align="left"><code>deb https://mirrors.ustc.edu.cn/termux/termux-packages-24 stable stable main</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/game-packages">Games</a></td>
<td align="left"><code>deb https://mirrors.ustc.edu.cn/termux/game-packages-24 games stable</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/termux-root-packages">Root</a></td>
<td align="left"><code>deb https://mirrors.ustc.edu.cn/termux/termux-root-packages-24 root stable</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/science-packages">Science</a></td>
<td align="left"><code>deb https://mirrors.ustc.edu.cn/termux/science-packages-24 science stable</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/unstable-packages">Unstable</a></td>
<td align="left"><code>deb https://mirrors.ustc.edu.cn/termux/unstable-packages unstable main</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/x11-packages">X11</a></td>
<td align="left"><code>deb https://mirrors.ustc.edu.cn/termux/x11-packages x11 main</code></td>
</tr>
</tbody>
</table>



<h2>
<a id="user-content-mirrors-by-xeffyr" class="anchor" href="#mirrors-by-xeffyr" aria-hidden="true"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"></path></svg></a>Mirrors by <a href="https://github.com/xeffyr">Xeffyr</a>
</h2>
<p>Only for installations running Android 7.0 and higher.</p>
<p>Uses IPFS for sole purpose of delegating repository hosting to "free" high performance hosts (aka "IPFS gateways"). Decentralization and persistence are not taken into account.</p>
<p>Also:</p>
<ul>
<li>Mirror is updated manually to ensure stability and gateway caching efficiency.</li>
<li>Mirror does not keep track of older package versions to optimize disk space usage.</li>
<li>Primary node can be shutdown during night times (22:00 - 09:00 UTC).</li>
</ul>
<p>Recommended IPFS gateways are:</p>
<ul>
<li><code>ipfs.io</code></li>
<li><code>10.via0.com</code></li>
<li><code>dweb.link</code></li>
</ul>
<p>You can try other gateways listed on <a href="https://ipfs.github.io/public-gateway-checker/" rel="nofollow">https://ipfs.github.io/public-gateway-checker/</a> or even setup your own.</p>
<table role="table">
<thead>
<tr>
<th align="left">Repository</th>
<th align="left">sources.list entry</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><a href="https://github.com/termux/termux-packages">Main</a></td>
<td align="left"><code>deb https://ipfs.io/ipns/k51qzi5uqu5dg9vawh923wejqffxiu9bhqlze5f508msk0h7ylpac27fdgaskx stable main</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/game-packages">Games</a></td>
<td align="left"><code>deb https://ipfs.io/ipns/k51qzi5uqu5dhngjg68o8x9uimwy5h8iqt91n2266idc7uet9ew3lc472upy27 games stable</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/termux-root-packages">Root</a></td>
<td align="left"><code>deb https://ipfs.io/ipns/k51qzi5uqu5dlp5yjlahzcp3kfpnhbifo9ka9iybo3bp5vt781duafkyyvt9al root stable</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/science-packages">Science</a></td>
<td align="left"><code>deb https://ipfs.io/ipns/k51qzi5uqu5dhvbtvdf46kkhobzgamhiirte6s6k28l2c1iapumphh3cpkw33f science stable</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/unstable-packages">Unstable</a></td>
<td align="left"><code>deb https://ipfs.io/ipns/k51qzi5uqu5dj05z8mr958kwvrg7a0wqouj5nnoo5uqu1btnsljvpznfaav9nk unstable main</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/x11-packages">X11</a></td>
<td align="left"><code>deb https://ipfs.io/ipns/k51qzi5uqu5dgu3homski160l4t4bmp52vb6dbgxb5bda90rewnwg64wnkwxj4 x11 main</code></td>
</tr>
</tbody>
</table>
<h2>
<a id="user-content-mirrors-by-the-tsinghua-university-tuna-association" class="anchor" href="#mirrors-by-the-tsinghua-university-tuna-association" aria-hidden="true"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"></svg></a>Mirrors by the <a href="https://tuna.moe/" rel="nofollow">Tsinghua University TUNA Association</a>
</h2>
<p>Mirror for Chinese users for better ping and download speed. Only for Android 7.0 and higher.</p>
<table role="table">
<thead>
<tr>
<th align="left">Repository</th>
<th align="left">sources.list entry</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><a href="https://github.com/termux/termux-packages">Main</a></td>
<td align="left"><code>deb https://mirrors.tuna.tsinghua.edu.cn/termux/termux-packages-24/ stable main</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/game-packages">Games</a></td>
<td align="left"><code>deb https://mirrors.tuna.tsinghua.edu.cn/termux/game-packages-24/ games stable</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/termux-root-packages">Root</a></td>
<td align="left"><code>deb https://mirrors.tuna.tsinghua.edu.cn/termux/termux-root-packages-24/ root stable</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/science-packages">Science</a></td>
<td align="left"><code>deb https://mirrors.tuna.tsinghua.edu.cn/termux/science-packages-24/ science stable</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/unstable-packages">Unstable</a></td>
<td align="left"><code>deb https://mirrors.tuna.tsinghua.edu.cn/termux/unstable-packages/ unstable main</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/x11-packages">X11</a></td>
<td align="left"><code>deb https://mirrors.tuna.tsinghua.edu.cn/termux/x11-packages/ x11 main</code></td>
</tr>
</tbody>
</table>
<h2>
<a id="user-content-mirrors-by-the-beijing-foreign-studies-university" class="anchor" href="#mirrors-by-the-beijing-foreign-studies-university" aria-hidden="true"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"></svg></a>Mirrors by the <a href="http://www.bfsu.edu.cn/" rel="nofollow">Beijing Foreign Studies University</a>
</h2>
<p>Mirror for Chinese users for better ping and download speed. Only for Android 7.0 and higher.</p>
<table role="table">
<thead>
<tr>
<th align="left">Repository</th>
<th align="left">sources.list entry</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><a href="https://github.com/termux/termux-packages">Main</a></td>
<td align="left"><code>deb https://mirrors.bfsu.edu.cn/termux/termux-packages-24/ stable main</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/game-packages">Games</a></td>
<td align="left"><code>deb https://mirrors.bfsu.edu.cn/termux/game-packages-24/ games stable</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/termux-root-packages">Root</a></td>
<td align="left"><code>deb https://mirrors.bfsu.edu.cn/termux/termux-root-packages-24/ root stable</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/science-packages">Science</a></td>
<td align="left"><code>deb https://mirrors.bfsu.edu.cn/termux/science-packages-24/ science stable</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/unstable-packages">Unstable</a></td>
<td align="left"><code>deb https://mirrors.bfsu.edu.cn/termux/unstable-packages/ unstable main</code></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/termux/x11-packages">X11</a></td>
<td align="left"><code>deb https://mirrors.bfsu.edu.cn/termux/x11-packages/ x11 main</code></td>
</tr>
</tbody>
</table>
