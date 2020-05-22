let teams = ['AGS','ATS','Alex von Falkenhausen Motorenbau','Alfa Romeo','AlphaTauri','Alta Car and Engineering Company','Andrea Moda','Arrows','Arzani Volpini','Aston Butterworth','Aston Martin','BAR','BRM','Benetton','Brabham','Brawn BGP','Bugatti Type','Caterham','Coloni','Cooper','Dallara','De Tomaso','Eagle','Ecurie Nationale Belge','Eisenacher Motorenwerk','Emeryson','Ensign','EuroBrun','Ferguson','Ferrari','Fittipaldi','Fondmetal','Footwork','Force India','Forti','Gilby Engineering','HRT','Haas','Hersham and Walton Motors','Hesketh','Hill','Hispania','Honda','JBW','Jaguar','Jordan','Klenk','Kurtis Kraft','Lambo','Lancia','Larrousse','Leyton House','Ligier','Lola','Lotus','Manor','March','Marussia','Maserati','Matra','McLaren','Mercedes','Merzario','Midland','Minardi','Osella','Pacific','Parnelli','Penske','Porsche','Prost','Racing Point','Red Bull','Renault','Rial','Sauber','Scuderia Milano','Shadow','Simtek','Spirit','Spyker','Stewart','Super Aguri','Surtees','Tec Mec','Toleman','Toro Rosso','Toyota','Tyrrell','Venturi','Veritas','Virgin','Williams','Wolf','Zakspeed'];
var dict = {
AGS: ['AGS JH21C - 1986', 'AGS JH22 - 1987', 'AGS JH23 - 1989', 'AGS JH24 - 1990'],
ATS: ['ATS D1 - 1978', 'ATS D2 - 1979', 'ATS D5 - 1982', 'ATS D6 - 1983', 'ATS D7 - 1984'],
Alex_von_Falkenhausen_Motorenbau: ['Alex von Falkenhausen Motorenbau - 1953'],
Alfa_Romeo: ['Alfa Romeo 158 159 Alfetta', 'Alfa Romeo 177 - 1979', 'Alfa Romeo 179 - 1982', 'Alfa Romeo 182 - 1982', 'Alfa Romeo 183T - 1983', 'Alfa Romeo 184T - 1985', 'Alfa Romeo 185T - 1985', 'Alfa Romeo Racing C38 - 2019', 'Alfa Romeo Racing C39 - 2020'],
AlphaTauri: ['AlphaTauri AT01 - 2020'],
Alta_Car_and_Engineering_Company: ['Alta Car and Engineering Company - 1952'],
Andrea_Moda: ['Andrea Moda S921 - 1992'],
Arrows: ['Arrows A1 - 1979', 'Arrows FA1 - 1978', 'Arrows A2 - 1979', 'Arrows A3 - 1981', 'Arrows A4 - 1982', 'Arrows A5 - 1982', 'Arrows A6 - 1984', 'Arrows A7 - 1984', 'Arrows A8 - 1986', 'Arrows A9 - 1986', 'Arrows A10 - 1988', 'Arrows A11 - 1991', 'Arrows A18 - 1997', 'Arrows A19 - 1998', 'Arrows A20 - 1999', 'Arrows A21 - 2000', 'Arrows A22 - 2001', 'Arrows A23 - 2002'],
Arzani_Volpini: [],
Aston_Butterworth: ['Aston Butterworth - 1952'],
Aston_Martin: ['Aston Martin DBR4 - 1960', 'Aston Martin DBR5 - 1960'],
BAR: ['BAR 01 - 1999', 'BAR 002 - 2000', 'BAR 003 - 2001', 'BAR 004 - 2002', 'BAR 005 - 2003', 'BAR 006 - 2004', 'BAR 007 - 2005'],
BRM: ['BRM Type 15 - 1951', 'BRM P30 - 1954', 'BRM P25 - 1960', 'BRM P48 - 1960', 'BRM P57 - 1965', 'BRM P61 - 1963', 'BRM P67 - 1964', 'BRM P261 - 1968', 'BRM P83 - 1967', 'BRM P115 - 1968', 'BRM P126 - 1969', 'BRM P133 - 1969', 'BRM P138 - 1969', 'BRM P139 - 1970', 'BRM P153 - 1972', 'BRM P160 - 1974', 'BRM P180 - 1972', 'BRM P201 - 1977', 'BRM P207 - 1977'],
Benetton: ['Benetton B186 - 1986', 'Benetton B187 - 1987', 'Benetton B188 - 1989', 'Benetton B189 - 1990', 'Benetton B190 - 1991', 'Benetton B191 - 1992', 'Benetton B192 - 1992', 'Benetton B193 - 1993', 'Benetton B194 - 1994', 'Benetton B195 - 1995', 'Benetton B196 - 1996', 'Benetton B197 - 1997', 'Benetton B198 - 1998', 'Benetton B199 - 1999', 'Benetton B200 - 2000', 'Benetton B201 - 2001'],
Brabham: ['Brabham BT3 - 1965', 'Brabham BT7 - 1966', 'Brabham BT10 - 1965', 'Brabham BT11 - 1968', 'Brabham BT19 - 1967', 'Brabham BT20 - 1969', 'Brabham BT24 - 1969', 'Brabham BT26 - 1971', 'Brabham BT34 - 1972', 'Brabham BT37 - 1973', 'Brabham BT44 - 1976', 'Brabham BT45 - 1978', 'Brabham BT46 - 1979', 'Brabham BT48 - 1979', 'Brabham BT49 - 1982', 'Brabham BT50 - 1982', 'Brabham BT52 - 1983', 'Brabham BT53 - 1984', 'Brabham BT54 - 1986', 'Brabham BT55 - 1986', 'Brabham BT56 - 1987', 'Brabham BT58 - 1990', 'Brabham BT59 - 1991', 'Brabham BT60 - 1992'],
Brawn_BGP: ['Brawn BGP 001 - 2009'],
Bugatti_Type: ['Bugatti Type 251 - 1956'],
Caterham: ['Caterham CT01 - 2012', 'Caterham CT03 - 2013', 'Caterham CT05 - 2014'],
Coloni: ['Coloni C3 - 1990', 'Coloni C4 - 1992'],
Cooper: ['Cooper Mark IV - 1950', 'Cooper T43 - 1960', 'Cooper T51 - 1963', 'Cooper T58 - 1961', 'Cooper T59 - 1965', 'Cooper T81 - 1968', 'Cooper T86 - 1969'],
Dallara: ['Dallara 3087 - 1988', 'Dallara F188 - 1988', 'Dallara F189 - 1989', 'Dallara F190 - 1990', 'Dallara F191 - 1991', 'Dallara F192 - 1992'],
De_Tomaso: ['De Tomaso 505 38'],
Eagle: ['Eagle Mk1 - 1969'],
Ecurie_Nationale_Belge: ['Ecurie Nationale Belge - 1962'],
Eisenacher_Motorenwerk: ['Eisenacher Motorenwerk - 1953'],
Emeryson: ['Emeryson - 1962'],
Ensign: ['Ensign N179 - 1979'],
EuroBrun: ['EuroBrun ER188 - 1989', 'EuroBrun ER189 - 1990'],
Ferguson: ['Ferguson P99 - 1961'],
Ferrari: ['Ferrari 125 F1 - 1952', 'Ferrari 375 F1 - 1951', 'Ferrari 212 F1 - 1953', 'Ferrari Tipo 500 - 1956', 'Ferrari 553 - 1954', 'Ferrari 246 F1 - 1960', 'Ferrari 246 P - 1960', 'Ferrari 156 F1 - 1964', 'Ferrari 158 - 1965', 'Ferrari 246 F1 66', 'Ferrari 312 - 1969', 'Ferrari 312B - 1975', 'Ferrari 312T - 1980', 'Ferrari 126C - 1984', 'Ferrari 156 85', 'Ferrari F1 86', 'Ferrari F1 87', 'Ferrari 640 - 1989', 'Ferrari 641 - 1990', 'Ferrari 642 - 1991', 'Ferrari 643 - 1991', 'Ferrari F92A - 1992', 'Ferrari F93A - 1993', 'Ferrari 412 T1 - 1994', 'Ferrari 412 T2 - 1995', 'Ferrari F310 - 1997', 'Ferrari F300 - 1998', 'Ferrari F399 - 1999', 'Ferrari F1 2000', 'Ferrari F2001 - 2002', 'Ferrari F2002 - 2003', 'Ferrari F2003 GA', 'Ferrari F2004 - 2005', 'Ferrari F2005 - 2005', 'Ferrari 248 F1 - 2006', 'Ferrari F2007 - 2007', 'Ferrari F2008 - 2008', 'Ferrari F60 - 2009', 'Ferrari F10 - 2010', 'Ferrari 150 Italia', 'Ferrari F2012 - 2012', 'Ferrari F138 - 2013', 'Ferrari F14 T - 2014', 'Ferrari SF15 T', 'Ferrari SF16 H', 'Ferrari SF70H - 2017', 'Ferrari SF71H - 2018', 'Ferrari SF90 - 2019', 'Ferrari SF1000 - 2020'],
Fittipaldi: ['Fittipaldi FD - 1977', 'Fittipaldi F5 - 1979', 'Fittipaldi F6 - 1979'],
Fondmetal: ['Fondmetal GR01 - 1992', 'Fondmetal GR02 - 1992'],
Footwork: ['Footwork FA12 - 1991', 'Footwork FA13 - 1993', 'Footwork FA14 - 1993', 'Footwork FA15 - 1994', 'Footwork FA16 - 1995', 'Footwork FA17 - 1996'],
Force_India: ['Force India VJM01 - 2008', 'Force India VJM02 - 2009', 'Force India VJM03 - 2010', 'Force India VJM04 - 2011', 'Force India VJM05 - 2012', 'Force India VJM06 - 2013', 'Force India VJM07 - 2014', 'Force India VJM08 - 2015', 'Force India VJM09 - 2016', 'Force India VJM10 - 2017', 'Force India VJM11 - 2018'],
Forti: ['Forti FG01 - 1996', 'Forti FG03 - 1996'],
Gilby_Engineering: ['Gilby Engineering - 1963'],
HRT: ['HRT F112 - 2012'],
Haas: ['Haas VF 16 - 2016', 'Haas VF 17 - 2017', 'Haas VF 18 - 2018', 'Haas VF 19 - 2019', 'Haas VF 20 - 2020'],
Hersham_and_Walton_Motors: ['Hersham and Walton Motors - 1955'],
Hesketh: ['Hesketh 308 - 1975', 'Hesketh 308C - 1976', 'Hesketh 308D - 1976', 'Hesketh 308E - 1978'],
Hill: ['Hill GH1 - 1975'],
Hispania: ['Hispania F110 - 2010', 'Hispania F111 - 2011'],
Honda: ['Honda RA271 - 1964', 'Honda RA272 - 1965', 'Honda RA273 - 1967', 'Honda RA300 - 1968', 'Honda RA301 - 1968', 'Honda RA302 - 1968', 'Honda RA106 - 2006', 'Honda RA107 - 2007', 'Honda RA108 - 2008'],
JBW: ['JBW - 1961'],
Jaguar: ['Jaguar R1 - 2000', 'Jaguar R2 - 2001', 'Jaguar R3 - 2002', 'Jaguar R4 - 2003', 'Jaguar R5 - 2004'],
Jordan: ['Jordan 191 - 1991', 'Jordan 192 - 1992', 'Jordan 193 - 1993', 'Jordan 194 - 1994', 'Jordan 195 - 1995', 'Jordan 196 - 1996', 'Jordan 197 - 1997', 'Jordan 198 - 1998', 'Jordan 199 - 1999', 'Jordan EJ10 - 2000', 'Jordan EJ11 - 2001', 'Jordan EJ12 - 2002', 'Jordan EJ13 - 2003', 'Jordan EJ14 - 2004', 'Jordan EJ15 - 2005'],
Klenk: ['Klenk - 1954'],
Kurtis_Kraft: ['Kurtis Kraft - 1959'],
Lambo: ['Lambo 291 - 1991'],
Lancia: ['Lancia D50 - 1956'],
Larrousse: ['Larrousse LH93 - 1993', 'Larrousse LH94 - 1994'],
Leyton_House: ['Leyton House CG901 - 1990', 'Leyton House CG911 - 1992'],
Ligier: ['Ligier JS5 - 1976', 'Ligier JS7 - 1978', 'Ligier JS9 - 1978', 'Ligier JS11 - 1980', 'Ligier JS17 - 1982', 'Ligier JS19 - 1982', 'Ligier JS21 - 1983', 'Ligier JS23 - 1984', 'Ligier JS25 - 1985', 'Ligier JS27 - 1986', 'Ligier JS29 - 1987', 'Ligier JS31 - 1988', 'Ligier JS33 - 1990', 'Ligier JS35 - 1991', 'Ligier JS37 - 1992', 'Ligier JS39 - 1994', 'Ligier JS41 - 1995', 'Ligier JS43 - 1996'],
Lola: ['Lola Mk4 - 1963', 'Lola T370 - 1975', 'Lola THL1 - 1986', 'Lola THL2 - 1986', 'Lola LC87 - 1987', 'Lola LC88 - 1989', 'Lola LC89 - 1990', 'Lola LC90 - 1990', 'Lola LC91 - 1991', 'Lola T93 30', 'Lola T97 30'],
Lotus: ['Lotus 12 - 1959', 'Lotus 16 - 1960', 'Lotus 18 - 1965', 'Lotus 18 21', 'Lotus 21 - 1965', 'Lotus 24 - 1965', 'Lotus 25 - 1967', 'Lotus 22 - 1965', 'Lotus 33 - 1967', 'Lotus 20 - 1965', 'Lotus 43 - 1967', 'Lotus 48 - 1967', 'Lotus 49 - 1970', 'Lotus 59 - 1969', 'Lotus 63 - 1969', 'Lotus 72 - 1975', 'Lotus 56 - 1971', 'Lotus 76 - 1974', 'Lotus 77 - 1976', 'Lotus 78 - 1978', 'Lotus 79 - 1979', 'Lotus 80 - 1979', 'Lotus 81 - 1981', 'Lotus 86 - 1980', 'Lotus 87 - 1982', 'Lotus 88 - 1981', 'Lotus 91 - 1982', 'Lotus 92 - 1983', 'Lotus 93T - 1983', 'Lotus 94T - 1983', 'Lotus 95T - 1984', 'Lotus 97T - 1985', 'Lotus 98T - 1986', 'Lotus 99T - 1987', 'Lotus 100T - 1988', 'Lotus 101 - 1989', 'Lotus 102 - 1992', 'Lotus 107 - 1994', 'Lotus 109 - 1994', 'Lotus T127 - 2010', 'Lotus T128 Formula One car ', 'Lotus E20 - 2012', 'Lotus E21 - 2013', 'Lotus E22 - 2014', 'Lotus E23 Hybrid - 2015'],
Manor: ['Manor MRT05 - 2016'],
March: ['March 701 - 1971', 'March 871 - 1987', 'March 881 - 1989', 'March CG891 - 1989'],
Marussia: ['Marussia MR01 - 2012', 'Marussia MR02 - 2013', 'Marussia MR03 - 2015'],
Maserati: ['Maserati 4CL and 4CLT - 1952', 'Maserati A6GCM - 1956', 'Maserati 250F - 1960'],
Matra: ['Matra MS5 - 1967', 'Matra MS7 - 1969', 'Matra MS9 - 1968', 'Matra MS10 - 1969', 'Matra MS11 - 1968', 'Matra MS80 - 1969', 'Matra MS84 - 1969', 'Matra MS120 - 1972'],
McLaren: ['McLaren M2B - 1966', 'McLaren M4B - 1967', 'McLaren M5A - 1968', 'McLaren M7A - 1971', 'McLaren M9A - 1969', 'McLaren M14A - 1971', 'McLaren M19A - 1973', 'McLaren M23 - 1978', 'McLaren M26 - 1979', 'McLaren M28 - 1979', 'McLaren M29 - 1981', 'McLaren M30 - 1980', 'McLaren MP4 1', 'McLaren MP4 2', 'McLaren MP4 3', 'McLaren MP4 4', 'McLaren MP4 5', 'McLaren MP4 6', 'McLaren MP4 7A', 'McLaren MP4 8', 'McLaren MP4 9', 'McLaren MP4 10', 'McLaren MP4 11', 'McLaren MP4 12', 'McLaren MP4 13', 'McLaren MP4 14', 'McLaren MP4 15', 'McLaren MP4 16', 'McLaren MP4 17', 'McLaren MP4 19', 'McLaren MP4 20', 'McLaren MP4 21', 'McLaren MP4 22', 'McLaren MP4 23', 'McLaren MP4 24', 'McLaren MP4 25', 'McLaren MP4 26', 'McLaren MP4 27', 'McLaren MP4 28', 'McLaren MP4 29', 'McLaren MP4 30', 'McLaren MP4 31', 'McLaren MCL32 - 2017', 'McLaren MCL33 - 2018', 'McLaren MCL34 - 2019', 'McLaren MCL35 - 2020'],
Mercedes: ['Mercedes Benz W196', 'Mercedes MGP W01 - 2010', 'Mercedes MGP W02 - 2011', 'Mercedes F1 W03 - 2012', 'Mercedes F1 W04 - 2013', 'Mercedes F1 W05 Hybrid - 2014', 'Mercedes F1 W06 Hybrid - 2015', 'Mercedes F1 W07 Hybrid - 2016', 'Mercedes AMG F1 W08 EQ Power - 2017', 'Mercedes AMG F1 W09 EQ Power - 2018', 'Mercedes AMG F1 W10 EQ Power - 2019', 'Mercedes AMG F1 W11 EQ Performance - 2020'],
Merzario: ['Merzario A2 - 1979', 'Merzario A4 - 1979'],
Midland: ['Midland M16 - 2006'],
Minardi: ['Minardi M185 - 1986', 'Minardi M186 - 1986', 'Minardi M187 - 1987', 'Minardi M188 - 1989', 'Minardi M189 - 1990', 'Minardi M190 - 1990', 'Minardi M191 - 1992', 'Minardi M192 - 1992', 'Minardi M193 - 1994', 'Minardi M194 - 1994', 'Minardi M195 - 1996', 'Minardi M197 - 1997', 'Minardi M198 - 1998', 'Minardi M01 - 1999', 'Minardi M02 - 2000', 'Minardi PS01 - 2001', 'Minardi PS02 - 2002', 'Minardi PS03 - 2003', 'Minardi PS04B - 2005', 'Minardi PS05 - 2005'],
Osella: ['Osella FA1L - 1988'],
Pacific: ['Pacific PR01 - 1994', 'Pacific PR02 - 1995'],
Parnelli: ['Parnelli VPJ4 - 1976'],
Penske: ['Penske PC1 - 1975', 'Penske PC3 - 1976', 'Penske PC4 - 1977'],
Porsche: ['Porsche 718 - 1964', 'Porsche 787 - 1962', 'Porsche 804 - 1962'],
Prost: ['Prost JS45 - 1997', 'Prost AP01 - 1998', 'Prost AP02 - 1999', 'Prost AP03 - 2000', 'Prost AP04 - 2001'],
Racing_Point: ['Racing Point RP19 - 2019', 'Racing Point RP20 - 2020'],
Red_Bull: ['Red Bull RB1 - 2005', 'Red Bull RB2 - 2006', 'Red Bull RB3 - 2007', 'Red Bull RB4 - 2008', 'Red Bull RB5 - 2009', 'Red Bull RB6 - 2010', 'Red Bull RB7 - 2011', 'Red Bull RB8 - 2012', 'Red Bull RB9 - 2013', 'Red Bull RB10 - 2014', 'Red Bull RB11 - 2015', 'Red Bull RB12 - 2016', 'Red Bull RB13 - 2017', 'Red Bull Racing RB14 - 2018', 'Red Bull Racing RB15 - 2019', 'Red Bull Racing RB16 - 2020'],
Renault: ['Renault RS01 - 1979', 'Renault RS10 - 1979', 'Renault RE20 - 1981', 'Renault RE30 - 1983', 'Renault RE40 - 1983', 'Renault RE50 - 1984', 'Renault RE60 - 1985', 'Renault R202 - 2002', 'Renault R23 - 2003', 'Renault R24 - 2004', 'Renault R25 - 2005', 'Renault R26 - 2006', 'Renault R27 - 2007', 'Renault R28 - 2008', 'Renault R29 - 2009', 'Renault R30 - 2010', 'Renault R31 - 2011', 'Renault R S 16 - 2016', 'Renault R S 17 - 2017', 'Renault R S 18 - 2018', 'Renault R S 19 - 2019', 'Renault R S 20 - 2020'],
Rial: ['Rial ARC1 - 1988', 'Rial ARC2 - 1989'],
Sauber: ['Sauber C12 - 1993', 'Sauber C13 - 1994', 'Sauber C14 - 1995', 'Sauber C15 - 1996', 'Sauber C16 - 1997', 'Sauber C17 - 1998', 'Sauber C18 - 1999', 'Sauber C19 - 2000', 'Sauber C20 - 2001', 'Sauber C21 - 2002', 'Sauber C22 - 2003', 'Sauber C23 - 2004', 'Sauber C24 - 2005', 'BMW Sauber F1 06', 'BMW Sauber F1 07', 'BMW Sauber F1 08', 'BMW Sauber F1 09', 'Sauber C29 - 2010', 'Sauber C30 - 2011', 'Sauber C31 - 2012', 'Sauber C32 - 2013', 'Sauber C33 - 2014', 'Sauber C34 - 2015', 'Sauber C35 - 2016', 'Sauber C36 - 2017', 'Sauber C37 - 2018'],
Scuderia_Milano: ['Scuderia Milano - 1950'],
Shadow: ['Shadow DN1 - 1973', 'Shadow DN3 - 1976', 'Shadow DN5 - 1977', 'Shadow DN7 - 1975', 'Shadow DN8 - 1978', 'Shadow DN9 - 1979'],
Simtek: ['Simtek S941 - 1994', 'Simtek S951 - 1995'],
Spirit: ['Spirit 201 - 1983', 'Spirit 101 - 1985'],
Spyker: ['Spyker F8 VII'],
Stewart: ['Stewart SF01 - 1997', 'Stewart SF02 - 1998', 'Stewart SF3 - 1999'],
Super_Aguri: ['Super Aguri SA05 - 2006', 'Super Aguri SA06 - 2006', 'Super Aguri SA07 - 2007', 'Super Aguri SA08 - 2008'],
Surtees: ['Surtees TS7 - 1971', 'Surtees TS9 - 1973', 'Surtees TS14 - 1973', 'Surtees TS16 - 1976', 'Surtees TS19 - 1978', 'Surtees TS20 - 1978'],
Tec_Mec: [],
Toleman: ['Toleman TG181 - 1982', 'Toleman TG183 - 1984', 'Toleman TG184 - 1984', 'Toleman TG185 - 1985'],
Toro_Rosso: ['Toro Rosso STR1 - 2006', 'Toro Rosso STR2 - 2008', 'Toro Rosso STR3 - 2008', 'Toro Rosso STR4 - 2009', 'Toro Rosso STR5 - 2010', 'Toro Rosso STR6 - 2011', 'Toro Rosso STR7 - 2012', 'Toro Rosso STR8 - 2013', 'Toro Rosso STR9 - 2014', 'Toro Rosso STR10 - 2015', 'Toro Rosso STR11 - 2016', 'Toro Rosso STR12 - 2017', 'Scuderia Toro Rosso STR13 - 2018', 'Scuderia Toro Rosso STR14 - 2019'],
Toyota: ['Toyota TF102 - 2002', 'Toyota TF103 - 2003', 'Toyota TF104 - 2004', 'Toyota TF105 - 2005', 'Toyota TF106 - 2006', 'Toyota TF107 - 2007', 'Toyota TF108 - 2008', 'Toyota TF109 - 2009'],
Tyrrell: ['Tyrrell 001 - 1971', 'Tyrrell 002 - 1972', 'Tyrrell 003 - 1972', 'Tyrrell 004 - 1974', 'Tyrrell 005 - 1974', 'Tyrrell 006 - 1974', 'Tyrrell 007 - 1977', 'Tyrrell P34 - 1977', 'Tyrrell 008 - 1978', 'Tyrrell 009 - 1980', 'Tyrrell 010 - 1981', 'Tyrrell 011 - 1983', 'Tyrrell 012 - 1985', 'Tyrrell 014 - 1986', 'Tyrrell 015 - 1986', 'Tyrrell DG016 - 1987', 'Tyrrell 017 - 1989', 'Tyrrell 018 - 1990', 'Tyrrell 019 - 1990', 'Tyrrell 020 - 1993', 'Tyrrell 021 - 1993', 'Tyrrell 022 - 1994', 'Tyrrell 023 - 1995', 'Tyrrell 024 - 1996', 'Tyrrell 025 - 1997', 'Tyrrell 026 - 1998'],
Venturi: ['Venturi LC92 - 1992'],
Veritas: ['Veritas automobile '],
Virgin: ['Virgin VR 01', 'Virgin MVR 02'],
Williams: ['Williams FW - 1975', 'Williams FW04 - 1977', 'Williams FW06 - 1979', 'Williams FW07 - 1982', 'Williams FW08 - 1983', 'Williams FW09 - 1984', 'Williams FW10 - 1985', 'Williams FW11 - 1987', 'Williams FW12 - 1989', 'Williams FW13 - 1990', 'Williams FW14 - 1992', 'Williams FW15C - 1993', 'Williams FW16 - 1994', 'Williams FW17 - 1995', 'Williams FW18 - 1996', 'Williams FW19 - 1997', 'Williams FW20 - 1998', 'Williams FW21 - 1999', 'Williams FW22 - 2000', 'Williams FW23 - 2001', 'Williams FW24 - 2002', 'Williams FW25 - 2003', 'Williams FW26 - 2004', 'Williams FW27 - 2005', 'Williams FW28 - 2006', 'Williams FW29 - 2007', 'Williams FW30 - 2008', 'Williams FW31 - 2009', 'Williams FW32 - 2010', 'Williams FW33 - 2011', 'Williams FW34 - 2012', 'Williams FW35 - 2013', 'Williams FW36 - 2014', 'Williams FW37 - 2015', 'Williams FW38 - 2016', 'Williams FW40 - 2017', 'Williams FW41 - 2018', 'Williams FW42 - 2019', 'Williams FW43 - 2020'],
Wolf: ['Wolf WR1 - 1978', 'Wolf WR5 - 1978', 'Wolf WR7 - 1980'],
Zakspeed: ['Zakspeed 841 - 1985', 'Zakspeed 861 - 1987', 'Zakspeed 871 - 1987', 'Zakspeed 881 - 1988', 'Zakspeed 891 - 1989'],
};



async function predict(image, f1_array){


    document.getElementById('app-gamef1-container-1').style.display = "none";
    document.getElementById('app-gamef1-container-2').style.display = "none";


    let new_canvas = document.createElement('canvas');
    await loadModel();

    // canvas dimensions
    new_canvas.height = image.height;
    new_canvas.width = image.width;
    new_canvas.getContext('2d').drawImage(image, 0, 0);

    // new resized canvas 28x28
    let resized_canvas = document.createElement('canvas');
    resized_canvas.width = 50;
    resized_canvas.height = 50;
    resized_canvas.getContext('2d').scale(50/image.width, 50/image.height);
    resized_canvas.getContext('2d').drawImage(new_canvas, 0, 0);


    let image_data = resized_canvas.getContext('2d').getImageData(0, 0, 50, 50);



    let input = tf.tensor4d(f1_array,[1,50,50,3]);

    // prediction
    console.log('Prediction started.'); // message
    let predictions = firstmodel.predict(input).dataSync(); // prediction
//    let predictions = firstmodel.predict(input).data(); // prediction
    console.log('Prediction completed.');// message
    console.log(predictions);
    const teams_predictions = predictions.slice().sort();
    console.log(teams_predictions);
//    console.log(predictions.sort()[predictions.length - 1]);
//    return predictions;
    let first_teams_predictions = teams_predictions[predictions.length - 1];
    let second_teams_predictions = teams_predictions[predictions.length - 2];

    let first_teams_result = predictions.indexOf(first_teams_predictions);
    let second_teams_result = predictions.indexOf(second_teams_predictions);

    console.log(teams[first_teams_result]);
    console.log(teams[second_teams_result]);

    team_result = document.getElementById('first_team');
    team_result.innerHTML = teams[first_teams_result];

    document.getElementById('first_team_b').innerHTML = teams[first_teams_result];

    document.getElementById('third_team').innerHTML = teams[second_teams_result];


    let folder = '../static/gamef1/modelsjs/'+teams[first_teams_result]+'/model.json';
    let folder_b = '../static/gamef1/modelsjs/'+teams[second_teams_result]+'/model.json';


    return [folder, folder_b]


};


function loadSelectTeams(){
    let select_team = document.getElementById("select-team");
    let options = teams.sort();
    for(var i = 0; i < options.length; i++) {
    var opt = options[i];
    var el = document.createElement("option");
    el.textContent = opt;
    el.value = opt;
    select_team.appendChild(el);
    };
    let select_chassis = document.getElementById("select-chassis");
    select_team.addEventListener("click", function(){

        for (i = select_chassis.options.length-1; i >= 1; i--) {
             select_chassis.options[i] = null;
        };

        var options_chassis = dict[select_team.value.replace(' ','_')];
        console.log(options_chassis);
        console.log(options_chassis.length);
        for(var i = 0; i < options_chassis.length; i++) {
        var opt_chassis = options_chassis[i];
        var el_chassis = document.createElement("option");
        el_chassis.textContent = opt_chassis;
        el_chassis.value = opt_chassis;
        select_chassis.appendChild(el_chassis);
        };
        document.getElementById("chassis").value = select_chassis.value;
        document.getElementById("team").value = select_team.value;

    });
    select_chassis.addEventListener("click", function(){
        document.getElementById("chassis").value = select_chassis.value;
        document.getElementById("team").value = select_team.value;


    });


};