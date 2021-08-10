from pytest import approx, fixture
from inst326_pytest_decorators import pts, num

from cities import Cities


CITY_DATA = """Zwijndrecht	51.21979	4.32664	18249
Zwijnaarde	51.00077	3.70746	7379
Zwevezele	51.03683	3.21186	5873
Zwevegem	50.81268	3.33848	23358
Zutendaal	50.93306	5.5753	6962
Zulte	50.91954	3.44859	14670
Zoutleeuw	50.83316	5.10376	7897
Zottegem	50.86955	3.81052	24434
Zonnebeke	50.8726	2.98725	11581
Zonhoven	50.99064	5.36819	19922
Zomergem	51.11994	3.56496	8158
Zolder	51.02455	5.30983	17289
Zoersel	51.26825	4.71296	10000
Zingem	50.90409	3.65305	6588
Zichem	51.00187	4.98316	6497
Zemst	50.98318	4.46079	21096
Zelzate	51.18963	3.80777	11901
Zellik	50.88408	4.27325	10874
Zele	51.06566	4.0403	20236
Zedelgem	51.14236	3.1368	21968
Zaventem	50.88365	4.47298	28188
Zandhoven	51.21488	4.66164	12306
Yvoir	50.3279	4.88059	8169
Wuustwezel	51.39214	4.59546	15000
Wondelgem	51.08705	3.70909	23546
Wommelgem	51.20452	4.5225	11917
Wolvertem	50.95172	4.30964	8045
Woluwe-Saint-Lambert	50.84389	4.42912	56584
Wingene	51.05782	3.27359	12887
Wilsele	50.89188	4.69769	9845
Wilrijk	51.16734	4.39513	41403
Willebroek	51.06041	4.36019	22808
Wijnegem	51.22787	4.51895	8932
Wielsbeke	50.9	3.36667	8828
Wichelen	51.00526	3.97683	11014
Wezembeek-Oppem	50.8395	4.49427	13245
Wevelgem	50.8	3.16667	30954
Wetteren	51.00526	3.88341	22930
Westmalle	51.29767	4.69013	8173
Westerlo	51.09049	4.91544	22579
Westende	51.15961	2.7687	5522
Wervik	50.78069	3.03854	17340
Wépion	50.42153	4.86403	6586
Wemmel	50.90812	4.30613	14406
Wellen	50.84096	5.33867	6804
Welkenraedt	50.6605	5.97034	9006
Wavre	50.71717	4.60138	32112
Watermael-Boitsfort	50.80154	4.41436	25157
Waterloo	50.71469	4.3991	29778
Wasmes	50.41464	3.8471	11731
Waremme	50.6976	5.25524	13737
Waregem	50.88898	3.42756	35896
Wanze	50.53907	5.20846	12918
Wanfercée-Baulet	50.47291	4.58748	7246
Wandre	50.66774	5.65959	6076
Walhain-Saint-Paul	50.62627	4.69837	5992
Walcourt	50.25401	4.43796	17501
Waimes	50.41488	6.11207	6661
Wachtebeke	51.16852	3.87183	6911
Waasmunster	51.10572	4.08573	10460
Waarschoot	51.1525	3.605	7762
Vottem	50.67155	5.57693	7478
Vosselaar	51.30856	4.8896	10317
Vorst	51.08029	5.01998	6824
Visé	50.7376	5.69907	17054
Virton	49.56824	5.53259	11259
Vilvoorde	50.92814	4.42938	36955
Villers-le-Bouillet	50.57708	5.25945	6059
Villers-la-Ville	50.57953	4.53398	9592
Vielsalm	50.28407	5.91502	7291
Veurne	51.07316	2.66803	11983
Verviers	50.58907	5.86241	52824
Veldegem	51.1048	3.1591	5189
Veerle	51.06989	4.98761	5748
Vedrin	50.50273	4.87604	7308
Vaux-sous-Chèvremont	50.60302	5.6335	6503
Varsenare	51.18981	3.13916	5081
Uitkerke	51.30684	3.13712	7863
Uccle	50.80225	4.33943	82929
Turnhout	51.32254	4.94471	44000
Tubize	50.69059	4.2009	18000
Trooz	50.57026	5.69521	7559
Tremelo	50.99231	4.70807	13721
Trazegnies	50.46379	4.3329	6798
Tournai	50.60715	3.38932	67721
Torhout	51.0656	3.10085	18933
Tongerlo	51.10622	4.91638	7404
Tongeren	50.78054	5.46484	29816
Tilff	50.56432	5.57642	5455
Tienen	50.80745	4.9378	31743
Tielt	50.99931	3.32707	19299
Tielt	50.9421	4.90505	5053
Thuin	50.33933	4.28604	14682
Theux	50.53323	5.81245	11587
Tessenderlo	51.06513	5.08856	16574
Tervuren	50.82372	4.51418	20623
Ternat	50.86654	4.16682	14569
Temse	51.12794	4.21372	26054
Tamines	50.43378	4.60713	7526
Strombeek-Bever	50.91039	4.35582	13727
Strépy-Bracquegnies	50.4728	4.12022	8880
Sterrebeek	50.86171	4.49375	8357
Stene	51.20437	2.91259	6310
Stembert	50.59107	5.89404	8696
Stekene	51.2099	4.03651	16989
Steenokkerzeel	50.91851	4.50989	10566
Stavelot	50.395	5.93124	6646
Staden	50.97456	3.01469	10786
Stabroek	51.33189	4.37127	17294
Sprimont	50.50922	5.6595	12945
Spa	50.48375	5.86674	10756
Soumagne	50.61385	5.74679	15237
Sombreffe	50.52865	4.60087	7452
Soignies	50.57904	4.07129	24869
Sleidinge	51.13363	3.67405	7640
Sint-Truiden	50.81679	5.18647	37859
Sint-Stevens-Woluwe	50.86838	4.45195	9038
Sint-Pieters-Leeuw	50.77926	4.24355	30446
Sint-Niklaas	51.16509	4.1437	69010
Sint-Michiels	51.18806	3.21142	12297
Sint-Martens-Lennik	50.81158	4.16965	8818
Sint-Martens-Latem	51.01459	3.63779	8303
Sint-Maria-Lierde	50.81867	3.84436	6449
Sint-Lievens-Houtem	50.9197	3.86225	9146
Sint-Lenaarts	51.34868	4.68009	6685
Sint-Laureins	51.24202	3.52441	6657
Sint-Kwintens-Lennik	50.80377	4.15489	5856
Sint-Kruis	51.21399	3.24949	16000
Sint-Katherina-Lombeek	50.87314	4.1536	6607
Sint-Katelijne-Waver	51.06691	4.53469	19487
Sint-Job-in-'t-Goor	51.29907	4.57289	8515
Sint-Gillis-Waas	51.21914	4.12374	17658
Sint-Gillis-bij-Dendermonde	51.01905	4.11146	12953
Sint-Genesius-Rode	50.74645	4.35754	17990
Sint-Denijs-Westrem	51.02135	3.67202	6419
Sint-Andries	51.19696	3.17891	19336
Sint-Amandsberg	51.05947	3.74943	32115
Sint-Amands	51.05645	4.20957	7653
Sinaai	51.15789	4.04087	6319
Silly	50.64877	3.92363	7887
Sijsele	51.20846	3.31714	5348
's-Gravenwezel	51.26267	4.56113	6379
Seraing	50.58362	5.50115	60737
Seneffe	50.53135	4.26301	11025
Seilles	50.50065	5.09268	5826
Schriek	51.02844	4.69357	5062
Schoten	51.25251	4.50268	33622
Schilde	51.24107	4.58336	20373
Scherpenheuvel	50.98075	4.97552	7162
Schepdaal	50.83836	4.19609	6004
Schelle	51.12615	4.34114	7675
Schaerbeek	50.86935	4.37737	132761
Sauvenière	50.58157	4.72466	5029
Saint-Vith	50.28146	6.12724	9135
Saint-Vaast	50.45426	4.16041	6351
Saint-Servais	50.4763	4.83656	9516
Saint-Nicolas	50.62837	5.53243	22586
Saint-Josse-ten-Noode	50.8538	4.37282	27366
Saint-Hubert	50.02668	5.37401	5538
Saint-Gilles	50.82763	4.34389	50221
Saint-Ghislain	50.44816	3.81886	22500
Saint-Georges-sur-Meuse	50.60007	5.3574	6803
Rumst	51.08153	4.42217	14521
Rumbeke	50.93248	3.16716	14265
Ruiselede	51.04039	3.39416	5129
Ruisbroek	50.79015	4.29771	7041
Ruddervoorde	51.09589	3.20743	5832
Roux	50.44111	4.3917	8983
Rotselaar	50.95302	4.71665	15007
Ronse	50.74574	3.6005	24204
Le Roeulx	50.50365	4.11163	7968
Roeselare	50.94653	3.12269	56016
Rocourt	50.67579	5.54621	7010
Rochefort	50.1631	5.2216	11978
Rixensart	50.71229	4.52529	21616
Rillaar	50.97376	4.89177	5518
Rijmenam	51.0016	4.58405	5755
Rijkevorsel	51.34795	4.76053	10606
Riemst	50.80995	5.60131	15809
Retie	51.26652	5.08242	8000
Remicourt	50.68069	5.32785	5050
Reet	51.10201	4.41264	6865
Rebecq-Rognon	50.65147	4.10683	10049
Ravels	51.37274	4.9921	13560
Ranst	51.18983	4.56533	17405
Ransart	50.46166	4.47616	8813
Ramillies	50.63395	4.90119	5749
Raeren	50.6672	6.11535	9925
Quiévrain	50.40737	3.68351	6560
Quévy-le-Petit	50.36879	3.93602	7689
Quaregnon	50.44067	3.8653	18491
Puurs	51.07409	4.28844	15944
Putte	51.05337	4.63263	15276
Profondeville	50.37581	4.86506	11401
Prayon	50.57795	5.6753	5240
Poperinge	50.85386	2.72659	19537
Pont-à-Celles	50.50518	4.36887	15909
Plombières	50.73656	5.95922	9596
Pittem	50.99279	3.26317	6589
Philippeville	50.19612	4.54374	8051
Lettelingen	50.68333	4.08333	6611
Petegem-aan-de-Leie	50.96667	3.53333	10332
Péruwelz	50.50819	3.59373	16647
Pepinster	50.56568	5.80386	9530
Peer	51.1303	5.45952	15551
Pâturages	50.4072	3.855	8106
Pamel	50.8453	4.07129	9241
Paliseul	49.90395	5.13537	5037
Paal	51.03988	5.17233	11935
Overpelt	51.21038	5.41557	13344
Overijse	50.77436	4.53461	23486
Oupeye	50.71184	5.6468	23594
Ougrée	50.60149	5.5444	11975
Oud-Turnhout	51.31978	4.9841	12354
Oud-Heverlee	50.83522	4.66421	10533
Oudenburg	51.18489	3.00035	8752
Oudenaarde	50.85168	3.60891	27935
Ottignies	50.66535	4.56679	9557
Opwijk	50.96724	4.18442	12045
Opglabbeek	51.04258	5.58346	9452
Oostrozebeke	50.92093	3.33799	7489
Oostmalle	51.3	4.73333	7034
Oostkamp	51.15432	3.23128	21489
Oostham	51.10374	5.17877	5320
Oosterzele	50.95261	3.79826	13151
Ostend	51.21551	2.927	69011
Oostduinkerke	51.11565	2.68217	8534
Oostakker	51.10124	3.76945	7885
Onze-Lieve-Vrouw-Waver	51.06265	4.57941	5621
Ohain	50.69885	4.4698	5977
Oedelem	51.17033	3.33762	6360
Noorderwijk	51.14122	4.84061	5166
Nivelles	50.59833	4.32848	24149
Ninove	50.82776	4.02657	34795
Nijlen	51.16096	4.67008	20792
Nieuwpoort	51.13008	2.75135	10845
Nieuwkerken-Waas	51.19358	4.17776	6082
Nieuwerkerken	50.92386	4.00433	6174
Nieuwerkerken	50.8638	5.19467	6466
Niel	51.11096	4.33428	8656
Nevele	51.03531	3.54574	11153
Neufchâteau	49.84074	5.43535	6416
Neerpelt	51.22807	5.4427	16122
Neeroeteren	51.09156	5.69933	9759
Brakel	50.80101	3.76264	6513
Nazareth	50.95686	3.59425	10890
Nassogne	50.12849	5.34274	5081
Namur	50.4669	4.86746	106284
Nalinnes	50.32434	4.44572	5785
Muizen	51.01111	4.51427	5386
Mouscron	50.74497	3.20639	52069
Mortsel	51.16697	4.45127	24525
Morlanwelz-Mariemont	50.45502	4.24519	18233
Moorslede	50.8919	3.06117	10720
Moorsele	50.8409	3.15971	6102
Moorsel	50.94743	4.09825	5103
Mont-sur-Marchienne	50.38997	4.40732	12761
Mont-Saint-Guibert	50.63427	4.61061	6557
Montignies-sur-Sambre	50.41081	4.49109	18765
Montigny-le-Tilleul	50.38056	4.37582	8938
Montegnée	50.64576	5.51411	11417
Mons	50.45413	3.95229	91277
Monceau-sur-Sambre	50.41694	4.37668	9812
Momignies	50.0271	4.16519	5183
Molenbeek-Saint-Jean	50.8499	4.31248	97037
Mol	51.19188	5.11662	32659
Moerbeke	51.17409	3.93001	5855
Middelkerke	51.18532	2.82077	17789
Meulebeke	50.95136	3.28804	10948
Mettet	50.32119	4.66232	12014
Messancy	49.59201	5.81879	7144
Merksplas	51.35851	4.86513	7963
Merksem	51.24623	4.44903	44435
Merelbeke	50.99447	3.74621	16684
Mere	50.92306	3.97134	5335
Merchtem	50.95129	4.23197	14660
Menen	50.79722	3.12245	31916
Melsele	51.22285	4.28201	10941
Melle	51.00232	3.80526	10687
Meise	50.93934	4.32655	18497
Meeuwen	51.0991	5.52106	5668
Meerhout	51.1321	5.07842	9346
Meerbeke	50.82444	4.03674	5866
Mechelen-aan-de-Maas	50.96589	5.69144	15374
Mechelen	51.02574	4.47762	77530
Maurage	50.45652	4.09704	5098
Marke	50.80678	3.23344	7575
Mariakerke	51.07476	3.68289	17062
Marcinelle	50.39216	4.44388	23696
Marchin	50.46707	5.2428	5063
Marchienne-au-Pont	50.40573	4.3953	15154
Marche-en-Famenne	50.22678	5.34416	16856
Manage	50.50312	4.23589	22196
Malonne	50.43969	4.79562	5467
Malmédy	50.42686	6.02794	11514
Maldegem	51.20737	3.44511	22092
Machelen	50.91061	4.44174	12252
Maasmechelen	50.96545	5.69452	36251
Maaseik	51.09802	5.78379	23684
Lummen	50.98772	5.19121	13689
Lubbeek	50.88278	4.83896	13574
Lovendegem	51.10168	3.61298	9272
Louvain-la-Neuve	50.66829	4.61443	29521
Lommel	51.23074	5.31349	31993
Lokeren	51.10364	3.99339	37567
Lodelinsart	50.43138	4.44886	8489
Lochristi	51.09644	3.83194	19696
Lobbes	50.35258	4.26716	5467
Lissewege	51.29427	3.19331	7699
Linden	50.89494	4.77027	5042
Limelette	50.68428	4.57186	5416
Limbourg	50.61222	5.9412	5612
Limal	50.69477	4.57538	9443
Lille	51.24197	4.82313	15466
Lier	51.13128	4.57041	33272
Liège	50.63373	5.56749	182597
Liedekerke	50.86892	4.08743	11980
Lichtervelde	51.03333	3.15	8169
Lichtaart	51.22495	4.91681	6212
Leval-Trahegnies	50.4213	4.22556	6473
Leuze	50.6	3.6	7095
Leuven	50.87959	4.70093	92892
Lessines	50.71104	3.83579	17687
Leopoldsburg	51.11667	5.25	14149
Lendelede	50.88626	3.23747	5393
Lemberge	50.97629	3.77054	6726
Lembeek	50.7157	4.21832	7689
Ledeberg	51.03859	3.74458	8454
Lede	50.96626	3.98594	16813
Lebbeke	51.00464	4.13457	17372
Lauwe	50.79479	3.1869	8392
Langemark	50.9131	2.91965	5079
Langdorp	50.99561	4.87175	7492
Landen	50.75267	5.082	14458
Lanaken	50.89318	5.6468	24771
La Louvière	50.48657	4.18785	76668
La Hulpe	50.73091	4.48577	7415
La Calamine	50.71809	6.01107	10232
La Bruyère	50.39478	4.61444	8194
La Bouverie	50.40524	3.8744	7169
Laarne	51.03078	3.85077	11600
Kwaadmechelen	51.10099	5.14478	5574
Kuurne	50.85143	3.2824	12638
Kuringen	50.94426	5.29902	11409
Kruishoutem	50.90168	3.52588	8179
Kruibeke	51.17048	4.31444	14815
Kraainem	50.86155	4.46946	12815
Kortrijk	50.82803	3.26487	73879
Kortessem	50.8589	5.38974	8042
Kortenberg	50.88982	4.54353	17774
Kortenaken	50.90862	5.05968	7374
Kortemark	51.02951	3.04112	11937
Kontich	51.13213	4.44706	20290
Koksijde	51.11642	2.63772	21027
Koersel	51.05909	5.27121	18076
Koekelberg	50.86117	4.33136	21984
Koekelare	51.09047	2.9783	8317
Knokke-Heist	51.35	3.26667	33781
Knokke	51.35113	3.28744	14449
Knesselare	51.13932	3.41282	7889
Klemskerke	51.24222	3.02401	6447
Kinrooi	51.14543	5.74207	11946
Kessel-Lo	50.88549	4.73717	30215
Kessel	51.13892	4.62962	7591
Kasterlee	51.24118	4.96651	17765
Kaprijke	51.2172	3.61519	6114
Kapelle-op-den-Bos	51.0097	4.36303	8859
Kapellen	51.31377	4.43539	26410
Kalmthout	51.38442	4.47556	17485
Kalken	51.03836	3.9186	5782
Kain	50.63869	3.39688	7412
Jurbise	50.531	3.90942	9483
Juprelle	50.7076	5.53127	8354
Jupille-sur-Meuse	50.64587	5.63307	10604
Jumet	50.4422	4.43745	24510
Jodoigne	50.72357	4.86914	11930
Jette	50.87309	4.33419	52490
Jemeppe-sur-Meuse	50.61701	5.49849	11312
Jemeppe-sur-Sambre	50.46543	4.6655	6127
Jemappes	50.44914	3.89096	10809
Jambes	50.45636	4.87166	19658
Jalhay	50.55876	5.96764	7688
Jabbeke	51.18185	3.08935	13488
Izegem	50.91396	3.21378	26382
Ixelles	50.83333	4.36667	86671
Ivoz-Ramet	50.58798	5.4657	5672
Ittre	50.64396	4.26476	6014
Itegem	51.10328	4.72855	5911
Ingelmunster	50.92081	3.25571	10603
Ieper	50.85114	2.88569	35089
Ichtegem	51.09572	3.01549	13582
Huy	50.51894	5.23284	19973
Huldenberg	50.78939	4.5831	9137
Hove	51.15446	4.4707	7968
Houthulst	50.97824	2.9505	8951
Houthalen	51.03427	5.37429	30050
Houdeng-Goegnies	50.49032	4.17513	14312
Houdeng-Aimeries	50.48132	4.14545	7534
Hornu	50.4328	3.82736	8793
Hoogstraten	51.40029	4.76034	18524
Hooglede	50.98333	3.08333	9900
Holsbeek	50.92097	4.75747	9094
Hollogne-aux-Pierres	50.64059	5.47179	14944
Hofstade	50.9613	4.02663	5927
Hoevenen	51.30604	4.40203	8473
Hoeselt	50.84714	5.48767	9265
Hoeilaart	50.7673	4.46835	10272
Hoboken	51.17611	4.34844	34443
Hingene	51.10345	4.26904	5047
Heverlee	50.86426	4.69597	23278
Hever	50.99545	4.55126	6426
Heusy	50.57457	5.86618	15420
Heusden	51.03664	5.28013	31017
Heusden	51.02815	3.80425	8606
Heule	50.83752	3.23818	11873
Herzele	50.88681	3.89014	16523
Herve	50.64083	5.79353	16544
Herstal	50.66415	5.62346	36503
Herselt	51.05159	4.88231	13493
Herseaux	50.71667	3.21667	9048
Herne	50.72423	4.03481	6459
Herk-de-Stad	50.94013	5.16636	11566
Herentals	51.17655	4.83248	25912
Herent	50.90861	4.67056	19218
Hensies	50.43263	3.68411	6390
Hemiksem	51.14484	4.33874	9504
Helchteren	51.05591	5.38244	30050
Hekelgem	50.90569	4.10769	5258
Heist-op-den-Berg	51.07537	4.72827	37873
Heist	51.33867	3.23882	12951
Heinsch	49.69986	5.7467	5470
Heers	50.75383	5.3021	6689
Hechtel	51.12518	5.36768	6605
Havré	50.46401	4.04675	6219
Hastière-Lavaux	50.21849	4.82446	5147
Hasselt	50.93106	5.33781	69222
Harelbeke	50.85343	3.30935	25978
Hannut	50.67142	5.07898	14129
Hamont	51.25332	5.54732	9001
Hamois	50.3402	5.15619	6662
Hamme	51.09822	4.13705	22891
Halle	51.24075	4.64327	7200
Halle	50.73385	4.23454	34479
Halen	50.94837	5.11096	8548
Haine-Saint-Pierre	50.45747	4.20659	7662
Haine-Saint-Paul	50.46185	4.1767	7268
Habay-la-Vieille	49.72329	5.61999	7704
Haaltert	50.90634	4.00093	17129
Gullegem	50.84301	3.20466	8888
Groot-Bijgaarden	50.87174	4.24973	8145
Grobbendonk	51.19043	4.73562	10724
Grivegnée	50.62148	5.61101	21057
Grimbergen	50.93409	4.37213	37000
Grez-Doiceau	50.73901	4.69829	12367
Grembergen	51.05406	4.10458	7080
Grâce-Berleur	50.64032	5.50329	10758
Gosselies	50.46936	4.43324	11017
Gooik	50.79443	4.11378	8957
Glabbeek	50.87267	4.95615	5070
Gistel	51.15612	2.96387	11084
Gingelom	50.74792	5.13422	7930
Gilly	50.42449	4.4789	20043
Ghlin	50.47313	3.90289	8485
Gesves	50.40146	5.07457	6150
Geraardsbergen	50.77343	3.88223	30807
Genval	50.72162	4.49375	8253
Gentbrugge	51.03692	3.76509	15885
Gent	51.05	3.71667	231493
Genk	50.965	5.50082	63666
Genappe	50.61173	4.45152	14266
Gembloux	50.56149	4.69889	21676
Geluwe	50.80978	3.07695	6757
Geetbets	50.89431	5.11199	5813
Geel	51.16557	4.98917	34697
Gavere	50.92917	3.66184	11888
Ganshoren	50.87065	4.31531	24859
Galmaarden	50.75389	3.97121	7939
Frasnes-lez-Buissenal	50.66783	3.62047	10936
Frameries	50.40578	3.89603	20598
Fosses-la-Ville	50.39517	4.69623	9062
Forêt	50.58387	5.7	5240
Forest	50.81678	4.32775	56254
Forchies-la-Marche	50.4369	4.32115	5649
Fontaine-l'Évêque	50.40907	4.32427	8730
Florenville	49.69983	5.3074	5464
Florennes	50.25127	4.60636	10723
Floreffe	50.43452	4.7596	7480
Fleurus	50.48351	4.55006	22080
Fléron	50.61516	5.68062	15994
Flénu	50.43673	3.88573	5704
Flémalle-Haute	50.59994	5.44471	25144
Flémalle-Grande	50.60906	5.47668	13738
Fayt-lez-Manage	50.48698	4.22959	6040
Farciennes	50.43006	4.54152	11488
Evergem	51.11306	3.70976	31615
Evere	50.87441	4.39905	41667
Eupen	50.6279	6.03647	18029
Etterbeek	50.83272	4.38835	48344
Étalle	49.67385	5.60019	5228
Estinnes-au-Val	50.41016	4.10477	7573
Estaimpuis	50.70485	3.26785	9340
Essen	51.46791	4.46901	10000
Esneux	50.53596	5.56775	13497
Ertvelde	51.17921	3.74722	10730
Erquelinnes	50.30688	4.11129	9396
Erps-Kwerps	50.90119	4.55984	6213
Erpe	50.93565	3.97219	5056
Erembodegem	50.91905	4.05041	12152
Engis	50.58156	5.39916	5737
Enghien	50.69375	4.03788	11367
Embourg	50.59043	5.6068	6124
Ellezelles	50.73512	3.67985	5566
Elewijt	50.96043	4.49684	5172
Eksel	51.15184	5.3906	5804
Eksaarde	51.14876	3.96814	6005
Ekeren	51.28087	4.41813	23300
Eke	50.95929	3.6396	5168
Eisden	50.98463	5.71433	10152
Éghezée	50.59076	4.91175	14352
Eernegem	51.1326	3.02562	7040
Eeklo	51.18703	3.55654	19116
Edegem	51.15662	4.44504	21839
Écaussinnes-d'Enghien	50.56822	4.1658	9802
Dworp	50.72983	4.30106	5470
Durbuy	50.35291	5.45631	10251
Duffel	51.09554	4.50903	16011
Drongen	51.05067	3.65649	13016
Dour	50.39583	3.77792	16861
Dottignies	50.73333	3.3	8299
Dison	50.61004	5.8534	13642
Dinant	50.25807	4.91166	12875
Dilsen	51.03718	5.72096	6099
Dilbeek	50.84799	4.25972	39482
Diksmuide	51.03248	2.86384	15515
Diest	50.98923	5.05062	22516
Diepenbeek	50.90769	5.41875	17699
Diegem	50.89727	4.43354	5001
Deurne	51.22134	4.46595	78747
Destelbergen	51.05952	3.79899	16853
Desselgem	50.88611	3.35958	5234
De Pinte	50.99339	3.64747	10020
De Panne	51.09793	2.59368	9799
Dendermonde	51.02869	4.10106	43055
Denderleeuw	50.88506	4.07601	16969
Denderhoutem	50.87234	4.01821	6000
Deinze	50.98175	3.53096	29815
De Haan	51.27261	3.03446	11766
Deerlijk	50.85337	3.35416	11292
Dampremy	50.41705	4.43092	6716
Damme	51.25147	3.28144	10924
Dalhem	50.71315	5.72774	6391
Cuesmes	50.43624	3.92323	9992
Couvin	50.05284	4.49495	13518
Court-Saint-Étienne	50.63378	4.56851	9353
Courcelles	50.46379	4.3747	29473
Couillet	50.39139	4.45908	11365
Comines	50.7754	3.00119	7899
Comblain-au-Pont	50.47488	5.57711	5308
Colfontaine	50.4141	3.85569	19964
Ciney	50.29449	5.10015	14830
Chimay	50.04856	4.31712	9720
Chièvres	50.58787	3.80711	6045
Chênée	50.612	5.6141	9163
Chaumont-Gistoux	50.67753	4.7212	10943
Chaudfontaine	50.5828	5.6341	20960
Châtelineau	50.41499	4.52016	17166
Châtelet	50.40338	4.52826	35238
Chastre-Villeroux-Blanmont	50.60857	4.64198	6243
Chasse Royale	50.42842	3.95001	0
Charleroi	50.41136	4.44448	200132
Chapelle-lez-Herlaimont	50.4713	4.28227	14353
Champion	50.4953	4.90385	5031
Céroux-Mousty	50.66089	4.5207	5397
Carnières	50.44428	4.25509	8087
Butgenbach	50.42689	6.20504	5516
Burcht	51.20393	4.34286	7494
Bullange	50.40731	6.25749	5340
Buizingen	50.74227	4.25278	6369
Buggenhout	51.0159	4.20173	13510
Brussels	50.85045	4.34878	1019022
Brunehault	50.50524	4.43209	7592
Brugge	51.20892	3.22424	116709
Bressoux	50.63988	5.60629	12588
Bree	51.14152	5.5969	14363
Bredene	51.23489	2.97559	14862
Brecht	51.35024	4.63829	14007
Brasschaat	51.2912	4.49182	37040
Braives	50.62848	5.14798	5672
Braine-le-Comte	50.60979	4.14658	20133
Braine-le-Château	50.6799	4.27385	9627
Braine-l'Alleud	50.68363	4.36784	37512
Bracquegnies	50.47094	4.1197	8880
Boutersem	50.84105	4.83367	7702
Boussu	50.43417	3.7944	20058
Bouillon	49.79324	5.06703	5347
Borsbeek	51.19661	4.48543	10334
Bornem	51.09716	4.24364	19997
Borgloon	50.80505	5.34366	9955
Borgerhout	51.20957	4.43539	46087
Boortmeerbeek	50.97929	4.57443	11570
Boom	51.09242	4.3717	15810
Booischot	51.05219	4.7751	6973
Boncelles	50.57108	5.53625	5578
Boechout	51.15959	4.49195	12145
Bocholt	51.17337	5.57994	12346
Blégny	50.67255	5.72508	12745
Blauwput	50.88587	4.72415	30215
Blankenberge	51.31306	3.13227	18000
Bissegem	50.82378	3.22844	5310
Binche	50.41155	4.16469	32030
Bilzen	50.87325	5.5184	29622
Bierbeek	50.82876	4.75949	8994
Beyne-Heusay	50.62251	5.66508	11608
Beverst	50.89091	5.47548	5483
Beverlo	51.08646	5.21855	8681
Beveren	51.21187	4.25633	45179
Beveren-Leie	50.87538	3.34034	5331
Bevere	50.8496	3.5873	15311
Bertrix	49.85596	5.25539	8063
Bertem	50.86403	4.62918	9215
Bernissart	50.4746	3.64961	11588
Berlare	51.03333	4	13853
Berlaar	51.1176	4.65835	10370
Beringen	51.04954	5.22606	40930
Berchem-Sainte-Agathe	50.86567	4.29557	25162
Berchem	51.19021	4.43264	43511
Belsele	51.14598	4.08859	10489
Beloeil	50.55047	3.73484	13405
Bekkevoort	50.94074	4.969	5714
Begijnendijk	51.01942	4.78377	9178
Beerzel	51.05753	4.67127	6077
Beersel	50.76589	4.3002	23228
Beerse	51.31927	4.85304	16208
Beernem	51.13981	3.33896	14512
Beauvechain	50.78195	4.7718	6334
Beauraing	50.11042	4.95554	8242
Beaumont	50.23699	4.23926	6645
Beaufays	50.55884	5.63881	5489
Bazel	51.14741	4.30129	5687
Baudour	50.48296	3.8332	6137
Battice	50.64734	5.82104	5691
Bastogne	50.00347	5.71844	14395
Bassenge	50.75883	5.60989	8151
Basse Lasne	50.69503	4.49218	13861
Balen	51.16837	5.17027	19978
Baasrode	51.03805	4.1546	6352
Baal	50.9955	4.75317	5931
Aywaille	50.47411	5.67684	10636
Awans	50.66774	5.46329	8612
Avelgem	50.77618	3.44502	9106
Auvelais	50.4504	4.63228	8456
Auderghem	50.81667	4.43333	33984
Aubange	49.56652	5.80492	14932
Athus	49.56475	5.83736	8028
Ath	50.62937	3.77801	26681
Assesse	50.36934	5.02204	6279
Assenede	51.22598	3.75085	13495
Assebroek	51.19367	3.2623	19772
Asse	50.91011	4.19836	28985
As	51.00755	5.58453	7250
Arlon	49.68333	5.81667	26179
Arendonk	51.32267	5.08289	12247
Ardooie	50.9757	3.19736	9161
Anzegem	50.837	3.47786	13920
Antwerpen	51.22047	4.40026	459805
Antoing	50.56765	3.4492	7507
Ans	50.6623	5.52029	27297
Anhée	50.31039	4.87827	7125
Angleur	50.6113	5.59942	10647
Andrimont	50.61298	5.88294	7064
Anderlues	50.40704	4.27136	11597
Anderlecht	50.83619	4.31454	160553
Andenne	50.48941	5.09513	24055
Amblève	50.35357	6.17002	5221
Amay	50.54829	5.30974	13307
Alsemberg	50.74134	4.33754	5943
Alleur	50.67465	5.51316	9768
Alken	50.87553	5.30558	10933
Aiseau	50.41158	4.58671	10906
Adegem	51.20509	3.4954	6473
Achel	51.253	5.47977	5365
Aartselaar	51.13412	4.38678	14193
Aarschot	50.98715	4.83695	27656
Aalter	51.09017	3.44693	18802
Aalst	50.93604	4.0355	77534
"""


@fixture
def cityobj(tmp_path):
    datapath = tmp_path / "tinydata.txt"
    datapath.write_text(CITY_DATA, encoding="utf-8")
    return Cities(str(datapath))


@num("1.1")
@pts(0.5)
def test_cities_exists(cityobj):
    """Do instances of Cities have a cities attribute?"""
    assert hasattr(cityobj, "cities"), \
        "instance of Cities class has no cities attribute"


@num("1.2")
@pts(0.5)
def test_cities_type(cityobj):
    """Is cities attribute a list?"""
    assert isinstance(cityobj.cities, list), "cities attribute is not a list"


@num("1.3")
@pts(0.5)
def test_cities_length(cityobj):
    """Does cities attribute contain the correct number of items?"""
    assert len(cityobj.cities) == CITY_DATA.count("\n"), \
        "cities attribute contains an unexpected number of items"


@num("1.4")
@pts(0.5)
def test_cities_contents(cityobj):
    """Is each item in cities attribute a dict as described in the assignment?"""
    for item in cityobj.cities:
        assert isinstance(item, dict), \
            "item in cities attribute is not a dict"
        assert set(item) == {"name", "lat", "lon", "pop"}, \
            "keys in dict in cities attribute do not match expected keys"
        assert isinstance(item["name"], str), \
            "value of 'name' key in dict should be a string"
        assert isinstance(item["lat"], float), \
            "value of 'lat' key in dict should be a float"
        assert isinstance(item["lon"], float), \
            "value of 'lon' key in dict should be a float"
        assert isinstance(item["pop"], int), \
            "value of 'pop' key in dict should be an int"

@num("1.5")
@pts(0.5)
def test_first_city(cityobj):
    """Do the values of cities[0] match what's in the file?"""
    assert cityobj.cities[0]["name"] == "Zwijndrecht", \
        "value of 'name' key does not match"
    assert cityobj.cities[0]["lat"] == approx(51.21979), \
        "value of 'lat' key does not match"
    assert cityobj.cities[0]["lon"] == approx(4.32664), \
        "value of 'lon' key does not match"
    assert cityobj.cities[0]["pop"] == 18249, \
        "value of 'pop' key does not match"

@num("2.1")
@pts(0.5)
def test_nearest1(cityobj):
    """Does nearest(50.32, 4.88) return the correct values?"""
    result = cityobj.nearest(50.32, 4.88)
    assert isinstance(result, list), \
        "nearest() method should return a list"
    assert len(result) == 10, \
        "unexpected number of items in list returned by nearest()"
    assert isinstance(result[0], dict), \
        "nearest() method should return a list of dicts"
    assert set(result[0]) == {"name", "lat", "lon", "pop"}, \
        "keys in dicts returned by nearest() do not match expected keys"
    expected = [
        {'name': 'Yvoir', 'lat': approx(50.3279), 'lon': approx(4.88059), 'pop': 8169},
        {'name': 'Anhée', 'lat': approx(50.31039), 'lon': approx(4.87827), 'pop': 7125},
        {'name': 'Profondeville', 'lat': approx(50.37581), 'lon': approx(4.86506), 'pop': 11401},
        {'name': 'Dinant', 'lat': approx(50.25807), 'lon': approx(4.91166), 'pop': 12875},
        {'name': 'Wépion', 'lat': approx(50.42153), 'lon': approx(4.86403), 'pop': 6586},
        {'name': 'Assesse', 'lat': approx(50.36934), 'lon': approx(5.02204), 'pop': 6279},
        {'name': 'Hastière-Lavaux', 'lat': approx(50.21849), 'lon': approx(4.82446), 'pop': 5147},
        {'name': 'Malonne', 'lat': approx(50.43969), 'lon': approx(4.79562), 'pop': 5467},
        {'name': 'Jambes', 'lat': approx(50.45636), 'lon': approx(4.87166), 'pop': 19658},
        {'name': 'Floreffe', 'lat': approx(50.43452), 'lon': approx(4.7596), 'pop': 7480}
    ]
    for actual, exp in zip(result, expected):
        assert actual == exp, "unexpected return value from nearest()"

@num("2.2")
@pts(0.5)
def test_nearest2(cityobj):
    """Does nearest(50.51894, 5.23284, min_population=50_000) return the correct values?"""
    result = cityobj.nearest(50.51894, 5.23284, min_population=50_000)
    expected = [
        {'name': 'Seraing', 'lat': approx(50.58362), 'lon': approx(5.50115), 'pop': 60737},
        {'name': 'Namur', 'lat': approx(50.4669), 'lon': approx(4.86746), 'pop': 106284},
        {'name': 'Liège', 'lat': approx(50.63373), 'lon': approx(5.56749), 'pop': 182597},
        {'name': 'Verviers', 'lat': approx(50.58907), 'lon': approx(5.86241), 'pop': 52824},
        {'name': 'Hasselt', 'lat': approx(50.93106), 'lon': approx(5.33781), 'pop': 69222},
        {'name': 'Genk', 'lat': approx(50.965), 'lon': approx(5.50082), 'pop': 63666},
        {'name': 'Leuven', 'lat': approx(50.87959), 'lon': approx(4.70093), 'pop': 92892},
        {'name': 'Charleroi', 'lat': approx(50.41136), 'lon': approx(4.44448), 'pop': 200132},
        {'name': 'Woluwe-Saint-Lambert', 'lat': approx(50.84389), 'lon': approx(4.42912), 'pop': 56584},
        {'name': 'Ixelles', 'lat': approx(50.83333), 'lon': approx(4.36667), 'pop': 86671}
    ]
    assert len(result) == len(expected), \
        "return value from nearest() has unexpected number of items"
    for actual, exp in zip(result, expected):
        assert actual == exp, "unexpected return value from nearest()"

@num("2.3")
@pts(0.5)
def test_nearest3(cityobj):
    """Does nearest(50.57, 5.7, 1) return the correct values?"""
    result = cityobj.nearest(50.57, 5.7, n=1)
    expected = [{'name': 'Trooz', 'lat': approx(50.57026), 'lon': approx(5.69521), 'pop': 7559}]
    assert len(result) == len(expected), \
        "return value from nearest() has unexpected number of items"
    for actual, exp in zip(result, expected):
        assert actual == exp, "unexpected return value from nearest()"

@num("2.4")
@pts(0.5)
def test_nearest4(cityobj):
    """Does nearest(50.85, 3.28, min_population=100_000, n=3) return the correct values?"""
    result = cityobj.nearest(50.85, 3.28, min_population=100_000, n=3)
    expected = [
        {'name': 'Gent', 'lat': approx(51.05), 'lon': approx(3.71667), 'pop': 231493},
        {'name': 'Brugge', 'lat': approx(51.20892), 'lon': approx(3.22424), 'pop': 116709},
        {'name': 'Anderlecht', 'lat': approx(50.83619), 'lon': approx(4.31454), 'pop': 160553}
    ]
    assert len(result) == len(expected), \
        "return value from nearest() has unexpected number of items"
    for actual, exp in zip(result, expected):
        assert actual == exp, "unexpected return value from nearest()"

@num("3.1")
@pts(0.25)
def test_cities_docstring_exists():
    """Does Cities class have a docstring?"""
    docstr = Cities.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "Cities class has no docstring"

@num("3.2")
@pts(0.25)
def test_cities_docstring_contents():
    """Does Cities class docstring have the correct sections?"""
    docstr = Cities.__doc__
    assert "Attributes:" in docstr, \
        "attack() method docstring has no 'Attributes:' section"

@num("3.3")
@pts(0.25)
def test_nearest_docstring_exists():
    """Does nearest() method have a docstring?"""
    docstr = Cities.nearest.__doc__
    assert isinstance(docstr, str) and len(docstr) > 0, \
        "Cities class has no docstring"

@num("3.4")
@pts(0.25)
def test_nearest_docstring_contents():
    """Does nearest() method docstring have the correct sections?"""
    docstr = Cities.nearest.__doc__
    assert "Args:" in docstr, \
        "nearest() method docstring has no 'Args:' section"
    assert "Returns:" in docstr, \
        "nearest() method docstring has no 'Returns:' section"
