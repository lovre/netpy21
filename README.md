# NetPy '21: Introduction to Network Science in Python

###### Workshop instructor

[Lovro Šubelj](http://lovro.fri.uni-lj.si), University of Ljubljana

###### Workshop schedule

Tuesday, 14th December 2021 at 4:00 PM (4 hours with breaks)

###### Workshop location

Lecture room 3 at [UL FRI](http://www.fri.uni-lj.si), Večna pot 113, Ljubljana, Slovenia

###### High-level description

This workshop is primarily aimed at Python programmers, either academics, professionals or students, that wish to learn the basics of modern network science and practical analyses of real networks, such as social, information and biological networks. Familiarity with the basics of probability theory and statistics, linear algebra, and machine learning is strongly encouraged.

The workshop is based on masters level course [Network Analysis](https://lovro.fri.uni-lj.si/posters/frinets.pdf) offered at the University of Ljubljana, Faculty of Computer and Information Science.

###### Recommended prerequisites

It is recommended that attendees bring a laptop with working installation of [Python](http://www.python.org), [NetworkX](http://networkx.github.io), [CDlib](http://cdlib.readthedocs.io) and [node2vec](https://snap.stanford.edu/node2vec/) packages. Alternatively, you can work with any other network analysis package such as [igraph](http://igraph.org), [graph-tool](http://graph-tool.skewed.de) or [SNAP.py](http://snap.stanford.edu/snappy/). For visualization of smaller networks, it is recommended to install some network analysis software such as [Gephi](http://gephi.org) or [visone](http://visone.info).

###### Tentative syllabus

+ **Challenge**: Warmup with four knights challenge (5 min)
1. From classical graph theory to **modern network science** (15 min)
2. **Large-scale structure** of real networks and **graph models** (45 min)
3. Measures of **node importance** and **link analysis** algorithms (45 min)
4. Network **community structure**, blockmodeling and **core-periphery** (45 min)
5. Network **visualization**, **machine learning** and some applications (45 min)

+ **Hands-on**: Abstraction, centrality, communities, visualization, learning etc. 

###### Networks data

All networks are available in Pajek, edge list in LNA formats.

+ [Simple toy example network](https://github.com/lovre/netpy21/blob/master/nets/toy.net) (5 nodes)
+ [Zachary's karate club network](https://github.com/lovre/netpy21/blob/master/nets/karate.net) (34 nodes)
+ [Davis's southern women network](https://github.com/lovre/netpy21/blob/master/nets/women.net) (32 nodes)
+ [Lusseau's bottlenose dolphins network](https://github.com/lovre/netpy21/blob/master/nets/dolphins.net) (62 nodes)
+ [Game of Thrones character appearance network](https://github.com/lovre/netpy21/blob/master/nets/got-appearance.net) (107 nodes)
+ [Human diseasome network by common symptoms](https://github.com/lovre/netpy21/blob/master/nets/diseasome.net) (117 nodes)
+ [Conflicts and alliances between world nations](https://github.com/lovre/netpy21/blob/master/nets/wars.net) (180 nodes)
+ [Game of Thrones character kills network](https://github.com/lovre/netpy21/blob/master/nets/got-kills.net) (284 nodes)
+ [Ljubljana public bus transport network](https://github.com/lovre/netpy21/blob/master/nets/lpp.net) (416 nodes)
+ [US airplane traffic transport network](https://github.com/lovre/netpy21/blob/master/nets/transport.net) (1,323 nodes)
+ [Java software class dependency network](https://github.com/lovre/netpy21/blob/master/nets/java.net) (1,516 nodes)
+ [Ingredients network by common compounds](https://github.com/lovre/netpy21/blob/master/nets/ingredients.net) (1,525 nodes)
+ [Map of Darknet from Tor network](https://github.com/lovre/netpy21/blob/master/nets/darknet.net) (7,178 nodes)
+ [IMDb actors collaboration network](https://github.com/lovre/netpy21/blob/master/nets/imdb.net) (17,577 nodes)
+ [Human protein-protein interaction network](https://github.com/lovre/netpy21/blob/master/nets/ppi.net) (19,634 nodes)
+ [WikiLeaks cable reference network](https://github.com/lovre/netpy21/blob/master/nets/wikileaks.net) (52,416 nodes)
+ [Internet map of autonomous systems](https://github.com/lovre/netpy21/blob/master/nets/internet.net) (75,885 nodes)
+ [Amazon product copurchase network](https://github.com/lovre/netpy21/blob/master/nets/amazon.net) (262,111 nodes)
+ [Paper citation network of APS](https://github.com/lovre/netpy21/blob/master/nets/aps.net) (438,943 nodes)
+ [Small part of Google web graph](https://github.com/lovre/netpy21/blob/master/nets/google.net) (875,713 nodes)
+ [Road/highway network of Texas](https://github.com/lovre/netpy21/blob/master/nets/texas.net) (1,379,917 nodes)

## Guimera's four knights challenge

Challenge will be **revealed in class** =)

![4knights](figs/4knights.png)

## 1. Classical graph theory → modern network science

###### Brief description

Introduction of networks and selected **motivational examples**. From **classical graph theory** to social network analysis and **modern network science**. Network perspectives in different **fields of science**.

![transportation](figs/transportation.png)

###### Lecture slides

+ [**Networks introduction and examples**](https://github.com/lovre/netpy21/blob/master/lectures/01-intro.pdf)
+ [**Historical development of network science**](https://github.com/lovre/netpy21/blob/master/lectures/02-history.pdf)
+ [**Network perspectives through science**](https://github.com/lovre/netpy21/blob/master/lectures/03-perspects.pdf) (tentative)

###### Book chapters

+ Ch. 1: [Introduction](http://networksciencebook.com/chapter/1) in Barabási, A.-L., [_Network Science_](http://networksciencebook.com) (Cambridge University Press, 2016).
+ Ch. 1-5: Introduction etc. in Newman, M.E.J., [_Networks: An Introduction_](https://global.oup.com/academic/product/networks-9780198805090?cc=si&lang=en&) (Oxford University Press, 2010).
+ Ch. 1: [Overview](https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch01.pdf) in Easley, D. & Kleinberg, J., [_Networks, Crowds, and Markets_](https://www.cs.cornell.edu/home/kleinber/networks-book/) (Cambridge University Press, 2010).

###### Selected must-reads

+ Barabási, A.-L., The network takeover, _Nat. Phys._ **8**(1), 14-16 (2012).
+ Motter, A.E. & Yang, Y., The unfolding and control of network cascades, _Phys. Today_ **70**(1), 33-39 (2017).
+ Cramer, C., Porter, M.A. et al., [_Network Literacy: Essential Concepts and Core Ideas_](https://sites.google.com/a/binghamton.edu/netscied/Network-Literacy-low-res.pdf?attredirects=0) (Creative Commons Licence, 2015).

###### Selected papers

+ Newman, M.E.J., The physics of networks, _Phys. Today_ **61**(11), 33-38 (2008).
+ Cimini, G., Squartini, T. et al., [The statistical physics of real-world networks](https://arxiv.org/abs/1810.05095), _Nat. Rev. Phys._ **1**(1), 58-71 (2019).
+ Newman, M.E.J., Communities, modules and large-scale structure in networks, _Nat. Phys._ **8**(1), 25-31 (2012).
+ Vespignani, A., Modelling dynamical processes in complex socio-technical systems, _Nat. Phys._ **8**(1), 32-39 (2012).
+ Hegeman, T. & Iosup, A., [Survey of graph analysis applications](https://arxiv.org/abs/1807.00382), e-print _arXiv:180700382v1_, pp. 23 (2018).
+ Hidalgo, C.A., Disconnected, fragmented, or united? A trans-disciplinary review of network science, _Appl. Netw. Sci._ **1**, 6 (2016).

## 2. Large-scale network structure and graph models

###### Brief description

Classical **graph theory** and modern **network analysis**. **Random graphs** and **network structure**, and scale-free and small-world networks. **Network representations**, data formats and repositories. 

![smallworld](figs/smallworld.png)

###### Lecture slides

+ [**Graph theory and network analysis**](https://github.com/lovre/netpy21/blob/master/lectures/04-networkology.pdf)
+ [**Random graphs and network structure**](https://github.com/lovre/netpy21/blob/master/lectures/05-randoms.pdf)
+ [**Scale-free and small-world networks**](https://github.com/lovre/netpy21/blob/master/lectures/06-models.pdf) (tentative)
+ [**Network representations, formats and data**](https://github.com/lovre/netpy21/blob/master/lectures/07-represent.pdf)

###### Hands-on analysis

+ [**Network structure and random graphs**](https://github.com/lovre/netpy21/blob/master/labs/structure.pdf) ([py](https://github.com/lovre/netpy21/blob/master/scripts/structure-starter.py))

###### Book chapters

+ Ch. 2: [Graph theory](http://networksciencebook.com/chapter/2), Ch. 3.8-3.9: [Small worlds etc.](http://networksciencebook.com/chapter/3) & Ch. 4-5: [Scale-free property etc.](http://networksciencebook.com/chapter/4) in Barabási, A.-L., Network Science (Cambridge University Press, 2016).
+ Ch. 6: Mathematics of networks & Ch. 12-15: Random graphs etc. in Newman, M.E.J., [_Networks: An Introduction_](https://global.oup.com/academic/product/networks-9780198805090?cc=si&lang=en&) (Oxford University Press, 2010).
+ Ch. 2: [Graphs](https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch02.pdf), Ch. 18: [Power laws etc.](https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch18.pdf) & Ch. 20: [Small-world phenomenon](https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch20.pdf) in Easley, D. & Kleinberg, J., Networks, Crowds, and Markets (Cambridge University Press, 2010).

###### Selected must-reads

+ Newman, M.E.J., Watts, D.J. & Strogatz, S.H., [Random graph models of social networks](https://www.pnas.org/content/pnas/99/suppl_1/2566.full.pdf?sid=2662d769-c2c0-48a5-afe5-6da549153812), _P. Natl. Acad. Sci. USA_ **99**, 2566-2572 (2002).
+ Ugander, J., Karrer, B. et al., [The anatomy of the Facebook social graph](https://arxiv.org/abs/1111.4503), e-print _arXiv:1111.4503v1_, pp. 17 (2011).
+ Backstrom, L., Boldi, P. et al., [Four degrees of separation](https://arxiv.org/abs/1111.4570), In: _Proceedings of WebSci '12_ (Evanston, IL, USA, 2012), pp. 45-54.

###### Selected papers

+ Erdős, P. & Rényi, A., [On random graphs I](http://ftp.math-inst.hu/~p_erdos/1959-11.pdf), _Publ. Math. Debrecen_ **6**, 290-297 (1959).
+ Milgram, S., The small world problem, Psychol. Today 1(1), 60-67 (1967). 
Granovetter, M.S., The strength of weak ties, _Am. J. Sociol._ **78**(6), 1360-1380 (1973).
+ Watts, D.J. & Strogatz, S.H., Collective dynamics of 'small-world' networks, _Nature_ **393**(6684), 440-442 (1998).
+ Barabási, A.-L. & Albert, R., Emergence of scaling in random networks, _Science_ **286**(5439), 509-512 (1999).
+ Faloutsos, M., Faloutsos, P. & Faloutsos, C., On power-law relationships of the Internet topology, _Comput. Commun. Rev._ **29**(4), 251-262 (1999).
+ Albert, R., Jeong, H. & Barabási, A.-L., Error and attack tolerance of complex networks, _Nature_ **406**(6794), 378-382 (2000).
+ Dorogovtsev, S.N. & Mendes, J.F.F., [Evolution of networks](https://arxiv.org/abs/cond-mat/0106144), _Adv. Phys._ **51**(4), 1079-1187 (2002).
+ Clauset, A., Shalizi, C.R. & Newman, M.E.J., [Power-law distributions in empirical data](https://arxiv.org/abs/0706.1062), _SIAM Rev._ **51**, 661-703 (2009).
+ De Domenico, M. & Arenas, A., [Modeling structure and resilience of the dark network](https://arxiv.org/abs/1612.01284), _Phys. Rev. E_ **95**(2), 022313 (2017).
+ Broido, A.D. & Clauset, A., [Scale-free networks are rare](https://www.nature.com/articles/s41467-019-08746-5), _Nat. Commun._ **10**(1), 1017 (2019).
+ Barabási, A.-L., [Love is all you need](https://uploads-ssl.webflow.com/58bcae2c9d6c401e73a26fed/5aa01d3e24eebb000199a0a2_loveisallyouneed.pdf), reply to e-print _arXiv:1801.03400v1_, pp. 6 (2018).
+ Holme, P., [Rare and everywhere](https://www.nature.com/articles/s41467-019-09038-8), _Nat. Commun._ **10**(1), 1016 (2019).

## 3. Measures of node importance and link analysis

###### Brief description

Node importance and **measures of centrality**, i.e. clustering coefficient, spectral analysis, closeness and betweenness centrality, and **link analysis** algorithms. Link importance and **measures of bridging**, i.e. betweenness, embeddedness and topological overlap.

![centrality](figs/centrality.png)

###### Lecture slides

+ [**Node importance and measures of centrality**](https://github.com/lovre/netpy21/blob/master/lectures/08-centrality.pdf)
+ [**Link analysis algorithms for web page importance**](https://github.com/lovre/netpy21/blob/master/lectures/09-analysis.pdf)
+ [**Link importance and measures of bridging**](https://github.com/lovre/netpy21/blob/master/lectures/10-bridging.pdf) (tentative)

###### Hands-on analysis

+ [**IMDb actors collaboration network**](https://github.com/lovre/netpy21/blob/master/labs/position.pdf) ([py](https://github.com/lovre/netpy21/blob/master/scripts/position-starter.py))

###### Book chapters

+ Ch. 7: Measures and metrics in Newman, M.E.J., [_Networks: An Introduction_](https://global.oup.com/academic/product/networks-9780198805090?cc=si&lang=en&) (Oxford University Press, 2010).
+ Ch. 14: [Link analysis and Web search](https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch14.pdf) in Easley, D. & Kleinberg, J., [_Networks, Crowds, and Markets_](https://www.cs.cornell.edu/home/kleinber/networks-book/) (Cambridge University Press, 2010).
+ Ch. 14-15: Classical node centrality etc. in Estrada, E. & Knight, P.A., [_A First Course in Network Theory_](https://global.oup.com/academic/product/a-first-course-in-network-theory-9780198726463?cc=si&lang=en&) (Oxford University Press, 2015).

###### Selected must-reads

+ Jeong, H., Mason, S.P. et al., Lethality and centrality in protein networks, _Nature_ **411**, 41-42 (2001).
+ Jensen, P., Morini, M. et al., [Detecting global bridges in networks](https://arxiv.org/abs/1509.08295), _J. Complex Netw._ **4**(3), 319-329 (2015).
+ Tong, H., Faloutsos, C. & Pan, J.-Y., Fast random walk with restart and its applications, In: _Proceedings of ICDM ’06_ (Washington, DC, USA, 2006), pp. 613-622.

###### Selected papers

+ Freeman, L., A set of measures of centrality based on betweenness, _Sociometry_ **40**(1), 35-41 (1977).
+ Bonacich, P., Power and centrality: A family of measures, _Am. J. Sociology_ **92**(5), 1170-1182 (1987).
+ Kleinberg, J., Authoritative sources in a hyperlinked environment, _J. ACM_ **46**(5), 604-632 (1999).
+ Franceschet, M. & Bozzo, E., [A theory on power in networks](https://arxiv.org/abs/1510.08332), e-print _arXiv:1510.08332v2_, pp. 19 (2016).
+ Everett, M.G. & Valente, T.W., Bridging, brokerage and betweenness, _Soc. Networks_ **44**, 202-208 (2016).
+ Berkhin, P., A survey on PageRank computing, _Internet Math._ **2**(1), 73-120 (2005).

### TBD