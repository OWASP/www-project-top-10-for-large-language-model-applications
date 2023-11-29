%%% ============================================================================
%%% This LaTeX document class is based on the LaTeX Templates port of the
%%% Legrand Orange Book Template by Mathias Legrand. It has been modified
%%% to meet the OWASP Documentation Project's style guide.
%%% The original template is available at:
%%% https://www.latextemplates.com/template/legrand-orange-book
%%%
%%% This template is licensed under a CC BY-NC-SA 4.0 license.
%%% To see what this license means for your use of the template, visit:
%%% https://creativecommons.org/licenses/by-nc-sa/4.0/
%%% ============================================================================

\def\headerimagefile{Header_Blue_Net}

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{owasp-doc}[2023-11-29 The OWASP Doc 0.1]
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{book}} % Pass through any options to the base class
\ProcessOptions\relax % Process given options
\LoadClass{book} % Load the base class

%-------------------------------------------------------------------------------
%	REQUIRED PACKAGES
%-------------------------------------------------------------------------------
\usepackage{graphicx}                           % Required for including pictures
\graphicspath{{assets/}}                        % Specifies the root path for images

\usepackage{float}                              % Required for controlling float positions
\usepackage[usenames, svgnames, table]{xcolor}  % Required for defining and using custom colors
\usepackage{calc}                               % Used for spacing the index letter headings correctly
\usepackage{changepage}                         % Required for temporarily indenting text blocks
\usepackage[toc]{appendix}                      % Required for the appendices chapters
\usepackage{etoolbox}                           % Required for conditional logic and easily changing commands
\usepackage{eso-pic}                            % Required for specifying an image background in the cover page
\usepackage[nochapter, tablegrid]{vhistory}     % Required for changelog
\usepackage{enumitem}         									% Customize lists
\setlist{nolistsep}           									% Reduce spacing between bullet points and numbered lists
% \usepackage{booktabs}                           % Required for nicer horizontal rules in tables
\usepackage{array}
\usepackage{longtable}                          % Tables which may stretch over more than 1 page
\usepackage{ltxtable}
\usepackage{tabularx}													 	% Required for tables with adjustable-width columns
\usepackage[none]{hyphenat}                     % Hyphenates words to split over two lines
\usepackage{listings}                           % Source code formatting and highlighting
\usepackage{color}                              % Required for syntax highlighting
\usepackage{colortbl}                           % Required for coloring table cells
\usepackage[skip=\baselineskip]{parskip}				% Required for sane paragraph spacing
\usepackage{lmodern}
\usepackage{kpfonts}
\usepackage[export]{adjustbox}

% ===================================================
% Color Definitions
% ===================================================

% branding -- uses hex values from libre office colors:
% https://github.com/LibreOffice/core/blob/master/extras/source/palettes/standard.soc
\definecolor{urlblue}{HTML}{3465a4}           % Dark Blue 1
\definecolor{owaspdarkpurple}{HTML}{5b277d}   % Dark Indigo 1
\definecolor{owasplightpurple}{HTML}{b7b3ca}  % Light Indigo 3
\definecolor{owasplightgrey}{HTML}{eeeeee}    % Light Grey 4
\definecolor{owaspdarkgrey}{HTML}{666666}     % Dark Grey 1
\definecolor{owaspred}{HTML}{f10d0c}          % Dark Red 1
\definecolor{owasporange}{HTML}{ea7500}       % Dark Orange 1
\definecolor{owaspyellow}{HTML}{ffff38}       % Light Yellow 1
\definecolor{owaspgold}{HTML}{ffbf00}         % Gold
\definecolor{owasplightgreen}{HTML}{5eb91e}   % Dark Lime 1
\definecolor{owaspdarkgreen}{HTML}{069a2e}    % Dark Green 1

% Syntax highlighting color scheme
% -- this is based on pygments defaults
% https://github.com/richleland/pygments-css/blob/master/default.css
\definecolor{Brown}{HTML}{773714}
\definecolor{OliveGreen}{HTML}{3d6624}
\definecolor{CadetBlue}{HTML}{244166}
\definecolor{nsclass}{HTML}{0000ff}
\definecolor{atnotation}{HTML}{008000}
\definecolor{comment}{HTML}{408080}
\definecolor{import}{HTML}{008000}
\definecolor{string}{HTML}{ba2121}
\definecolor{class}{HTML}{0000ff}
\definecolor{custommethod}{HTML}{008000}

% Misc. colors
\definecolor{Apricot}{HTML}{ffb786}

% Vulnerability header colors
% \definecolor{vcrit}{HTML}{e50000}
% \definecolor{vhigh}{HTML}{e52d00}
% \definecolor{vmed}{HTML}{dde500}
% \definecolor{vlow}{HTML}{7ee500}
% \definecolor{vinfo}{HTML}{aaaaaa}

% allow bold font to be colored
% example: \colorbf{owaspdarkpurple}{some purple bold text}
\newcommand\owaspbf[1]{\textcolor{owaspdarkpurple}{\textbf{#1}}}


%-------------------------------------------------------------------------------
%	MARGINS
%-------------------------------------------------------------------------------
\usepackage{geometry} % Required for adjusting page dimensions and margins
\geometry{
	top=3cm,            % Top margin
	bottom=2.5cm,       % Bottom margin
	inner=3cm,          % Inner margin (left on odd pages, right on even or left in oneside mode)
	outer=3cm,          % Outer margin (right on odd pages, left on even or right in oneside mode)
	headsep=10pt,       % Space from the top margin to the baseline of the header
	headheight=0.5cm,   % Header height
	footskip=1.4cm,     % Space from the bottom margin to the baseline of the footer
	columnsep=1cm,      % Horizontal space between columns when in two column mode
	%showframe,         % Uncomment to show how the type block is set on the page
}

\setlength{\parindent}{0pt} % Disable paragraph indentation



%-------------------------------------------------------------------------------
%	FONTS
%-------------------------------------------------------------------------------
% \usepackage{avant}            	% Use the Avantgarde font for headings
\usepackage[sfdefault]{roboto} 	% Use the Roboto font by default
\usepackage{microtype}        	% Improve typography
\usepackage[utf8]{inputenc}   	% Required for inputting international characters
\usepackage[T1]{fontenc}      	% Output font encoding for international characters
\usepackage{mathptmx}         	% Use the Adobe Times Roman as the default text font
                              	% together with math symbols from the Symbol, Chancery
                              	% and Computer Modern fonts

% adds the OWASP logo to the bottom corner of the page
\newcommand{\owasplogobottomright}{%
	\AddToShipoutPicture*{\put(386,5){\includegraphics[width=80mm]{owasp_logo.png}}}
}

% creates the header image on new sections
\newcommand{\headerimage}{%
	\clearpage
	\AddToShipoutPicture*{%
		\AtPageUpperLeft{%
			\raisebox{-\height}{%
				\includegraphics[width=\paperwidth, height=1in]{\headerimagefile}%
			}%
		}%
	}%
}

%----------------------------------------------------------------------------------------
%	HEADERS AND FOOTERS
%----------------------------------------------------------------------------------------

\usepackage{fancyhdr}         % Required for customizing headers and footers
\pagestyle{fancy}             % Enable the custom headers and footers

% Top horizontal rule thickness
\renewcommand{\headrulewidth}{0.5pt}

% Redefine the styling of the current chapter name in the header
\renewcommand{\chaptermark}[1]{\markboth{\sffamily\normalsize\bfseries\chaptername\ \thechapter.~#1}{}}

% Redefine the styling of the current section name in the header
\renewcommand{\sectionmark}[1]{\markright{\sffamily\normalsize\thesection~#1}{}}

% Clear default headers and footers
\fancyhf{}

\fancyhead[LE, RO]{\sffamily\thepage} % Header for left even pages and right odd pages
\fancyhead[LO]{\rightmark}            % Header for left odd pages
\fancyhead[RE]{\leftmark}             % Header for right even pages

% Style for when a plain pagestyle is specified
\fancypagestyle{plain}{
	\fancyhead{}                        % Clear headers
	\renewcommand{\headrulewidth}{0pt}  % Remove header rule
}

\usepackage{emptypage}                % removes headers and footers on empty pages between chapters


%----------------------------------------------------------------------------------------
%	SECTION STYLING
%----------------------------------------------------------------------------------------

\setcounter{secnumdepth}{3} % Number sections down to subsubsections, a value of 2 will number to subsections only and 1 to sections only

\usepackage[
	explicit, 	% Specify section names explicitly in \titleformat with #1
	newparttoc, % Required for writing the part toc entry number in a standard way (overriding default LaTeX behavior) so the titletoc package can style it
]{titlesec} 	% Required for modifying sections

%-------------------------------------------

% % Command to create and output the parts pages
% \newcommand{\outputpartpage}[2]{
% 	\begin{tikzpicture}[remember picture, overlay]
% 		\node[anchor=center, rectangle, fill=owaspdarkpurple!20, inner sep=0pt, minimum height=\paperheight, minimum width=\paperwidth] at (current page.center) {}; % Background color
% 		\node[anchor=north west, inner sep=0pt, xshift=\Gm@lmargin, yshift=-\Gm@tmargin] at (current page.north west) {\fontsize{220pt}{220pt}\selectfont\sffamily\bfseries\textcolor{owaspdarkpurple!40}{#1}}; % Part number
% 		\node[anchor=north east, inner sep=0pt, xshift=-\Gm@rmargin, yshift=-\Gm@tmargin] at (current page.north east) {\fontsize{30pt}{30pt}\selectfont\sffamily\bfseries\textcolor{white}{\strut #2}}; % Part title
% 		\node[anchor=south east, inner sep=0pt, xshift=-\Gm@rmargin, yshift=\Gm@bmargin] at (current page.south east) { % Mini table of contents
% 			\parbox[t][][t]{8.5cm}{ % Width of box holding the mini ToC
% 				\printcontents[part]{l}{0}{\setcounter{tocdepth}{1}} % Display the mini table of contents showing chapters and sections, change tocdepth to 2 to also show subsections or 0 to only show chapters
% 			}
% 		};
% 	\end{tikzpicture}
% }

\titleformat
	{\chapter} % Section type being modified
	[block] % Shape type, can be: hang, block, display, runin, leftmargin, rightmargin, drop, wrap, frame
	{} % Format of the whole section
	{\filright\huge \textcolor{owaspdarkpurple}{#1}} % Format of the section label
	{0em} % Space between the title and label
	{} % Code before the label
	[] % Code after the label

%-------------------------------------------

\titleformat
	{\section} % Section type being modified
	[block] % Shape type, can be: hang, block, display, runin, leftmargin, rightmargin, drop, wrap, frame
	{\bfseries\sffamily\Large} % Format of the whole section
	{\llap{{}\hspace{1em}} #1} % Format of the section label
	{0cm} % Space between the title and label
	{} % Code before the label
	[] % Code after the label

\titleformat
	{name=\section, numberless} % Section type being modified
	[block] % Shape type, can be: hang, block, display, runin, leftmargin, rightmargin, drop, wrap, frame
	{\bfseries\sffamily\Large} % Format of the whole section
	{#1} % Format of the section label
	{0cm} % Space between the title and label
	{} % Code before the label
	[] % Code after the label

\titlespacing*{\section}{0pt}{12pt}{6pt} % Spacing around section titles, the order is: left, before and after

%-------------------------------------------

\titleformat
	{\subsection} % Section type being modified
	[block] % Shape type, can be: hang, block, display, runin, leftmargin, rightmargin, drop, wrap, frame
	{\bfseries\sffamily\large} % Format of the whole section
	{\llap{\textcolor{owaspdarkpurple}{\thesubsection}\hspace{1em}}#1} % Format of the section label
	{0cm} % Space between the title and label
	{} % Code before the label
	[] % Code after the label

\titleformat
	{name=\subsection, numberless} % Section type being modified
	[block] % Shape type, can be: hang, block, display, runin, leftmargin, rightmargin, drop, wrap, frame
	{\bfseries\sffamily\large} % Format of the whole section
	{#1} % Format of the section label
	{0cm} % Space between the title and label
	{} % Code before the label
	[] % Code after the label

\titlespacing*{\subsection}{0pt}{12pt}{4pt} % Spacing around section titles, the order is: left, before and after

%-------------------------------------------

\titleformat
	{\subsubsection} % Section type being modified
	[block] % Shape type, can be: hang, block, display, runin, leftmargin, rightmargin, drop, wrap, frame
	{\bfseries\sffamily} % Format of the whole section
	{\llap{{\thesubsubsection}\hspace{1em}}#1} % Format of the section label
	{0cm} % Space between the title and label
	{} % Code before the label
	[] % Code after the label

\titleformat
	{name=\subsubsection, numberless} % Section type being modified
	[block] % Shape type, can be: hang, block, display, runin, leftmargin, rightmargin, drop, wrap, frame
	{\bfseries\sffamily} % Format of the whole section
	{#1} % Format of the section label
	{0cm} % Space between the title and label
	{} % Code before the label
	[] % Code after the label

\titlespacing*{\subsubsection}{0pt}{8pt}{4pt} % Spacing around section titles, the order is: left, before and after

%-------------------------------------------

\titleformat
	{\paragraph} % Section type being modified
	[runin] % Shape type, can be: hang, block, display, runin, leftmargin, rightmargin, drop, wrap, frame
	{\bfseries\sffamily} % Format of the whole section
	{} % Format of the section label
	{0cm} % Space between the title and label
	{#1} % Code before the label
	[] % Code after the label

\titlespacing*{\paragraph}{0pt}{0pt}{6pt} % Spacing around section titles, the order is: left, before and after

%----------------------------------------------------------------------------------------
%	TABLE OF CONTENTS
%----------------------------------------------------------------------------------------
\usepackage{titletoc} % Required for manipulating the table of contents
\setcounter{tocdepth}{2} % Display down to subsections in the table of contents
\contentsmargin{0cm} % Removes the default right margin

%------------------------------------------------

% Styling of numbered parts in the table of contents
\newcommand{\tocentrypartnumbered}[1]{%
	\setlength\fboxsep{0pt}% Remove box padding
	\contentslabel[%
		% Part number box
		\colorbox{owaspdarkpurple!20}{% Background color
			\strut\parbox[c][.7cm]{1.1cm}{% Box size
				\color{owaspdarkpurple!70}\Large\sffamily\bfseries\centering\thecontentslabel% Part number
			}%
		}%
		\hspace{4pt}%
		% Part title box
		\colorbox{owaspdarkpurple!40}{% Background color
			\strut\parbox[c][.7cm]{\linewidth-1.25cm}{% Box size
				\centering\Large\sffamily #1% Part title
			}%
		}%
	]{1.25cm}
}

% Styling of unnumbered parts in the table of contents
\newcommand{\tocentrypartunnumbered}[1]{%
	\setlength\fboxsep{0pt}% Remove box padding
	\contentslabel[%
		% Part title box
		\colorbox{owaspdarkpurple!40}{% Background color
			\strut\parbox[c][.7cm]{\linewidth}{% Box size
				\centering\Large\sffamily #1% Part title
			}%
		}%
	]{1.25cm}
}

\titlecontents{part} % Section type being modified
	[1.25cm] % Left indentation
	{\addvspace{20pt}\Large\sffamily\bfseries\hypersetup{linkcolor=black}} % Before code
	{\tocentrypartnumbered} % Formatting of numbered sections of this type
	{\tocentrypartunnumbered} % Formatting of numberless sections of this type
	{} % Formatting of the filler to the right of the heading and the page number
	[] % After code

%------------------------------------------------

\titlecontents{chapter} % Section type being modified
	[1.25cm] % Left indentation
	{\addvspace{12pt}\large\sffamily\bfseries\hypersetup{linkcolor=owaspdarkpurple}} % Before code
	{\color{owaspdarkpurple}\contentslabel[\Large\thecontentslabel]{1.25cm}} % Formatting of numbered sections of this type
	{} % Formatting of numberless sections of this type
	{\color{owaspdarkpurple!60}\normalsize\;\titlerule*[6pt]{.}\;\color{owaspdarkpurple}\thecontentspage} % Formatting of the filler to the right of the heading and the page number
	[] % After code

%------------------------------------------------

\titlecontents{section} % Section type being modified
	[1.25cm] % Left indentation
	{\addvspace{3pt}\sffamily\bfseries} % Before code
	{\contentslabel[\thecontentslabel]{1.25cm}} % Formatting of numbered sections of this type
	{} % Formatting of numberless sections of this type
	{~{\normalfont\titlerule*[6pt]{.}}~\thecontentspage} % Formatting of the filler to the right of the heading and the page number
	[] % After code

%------------------------------------------------

\titlecontents{subsection} % Section type being modified
	[1.25cm] % Left indentation
	{\addvspace{1pt}\sffamily\small} % Before code
	{\contentslabel[\thecontentslabel]{1.25cm}} % Formatting of numbered sections of this type
	{} % Formatting of numberless sections of this type
	{~\titlerule*[6pt]{.}~\thecontentspage} % Formatting of the filler to the right of the heading and the page number
	[] % After code

%------------------------------------------------

\titlecontents{subsubsection} % Section type being modified
	[1.75cm] % Left indentation
	{\sffamily\small} % Before code
	{\contentslabel[\thecontentslabel]{1.75cm}} % Formatting of numbered sections of this type
	{} % Formatting of numberless sections of this type
	{~\titlerule*[6pt]{.}~\thecontentspage} % Formatting of the filler to the right of the heading and the page number
	[] % After code

%------------------------------------------------

% List of figures entries
\titlecontents{figure} % Section type being modified
	[0cm] % Left indentation
	{\addvspace{2pt}\sffamily\small} % Before code
	{\thecontentslabel\hspace*{1em}} % Formatting of numbered sections of this type
	{} % Formatting of numberless sections of this type
	{~\titlerule*[6pt]{.}~\thecontentspage} % Formatting of the filler to the right of the heading and the page number
	[] % After code

%------------------------------------------------

% List of tables entries
\titlecontents{table} % Section type being modified
	[0cm] % Left indentation
	{\addvspace{2pt}\sffamily\small} % Before code
	{\thecontentslabel\hspace*{1em}} % Formatting of numbered sections of this type
	{} % Formatting of numberless sections of this type
	{~\titlerule*[6pt]{.}~\thecontentspage} % Formatting of the filler to the right of the heading and the page number
	[] % After code


%----------------------------------------------------------------------------------------
%	INDEX
%----------------------------------------------------------------------------------------

\usepackage{makeidx} % Required to make an index

\makeindex % Tells LaTeX to create the files required for indexing

% Modify the command to output the index to output the correctly styled Index name to the page headers
\patchcmd{\theindex}
	{\MakeUppercase\indexname} % Find
	{\sffamily\normalsize\bfseries\indexname} % Replace
	{}
	{}

%----------------------------------------------------------------------------------------
%	 TABLES
%----------------------------------------------------------------------------------------

% \usepackage{array} % Required for manipulating table elements

% \newcolumntype{R}[1]{>{\raggedleft\arraybackslash}p{#1}} % Define a new right-aligned paragraph column type
% \newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}} % Define a new left-aligned (no justification) paragraph column type
% \newcolumntype{C}[1]{>{\centering\arraybackslash}p{#1}} % Define a new centered paragraph column type

%----------------------------------------------------------------------------------------
%	 LISTS
%----------------------------------------------------------------------------------------

\usepackage{enumitem} % Required for list customization
\setlist{} % Customize spacing inside and outside lists

\renewcommand{\labelenumi}{\arabic{enumi}.} % Customize the first level numbered list characters
\renewcommand{\labelenumii}{\alph{enumii}.} % Customize the second level numbered list characters
\renewcommand{\labelenumiii}{\roman{enumiii}.} % Customize the third level numbered list characters

%------------------------------------------------

\renewcommand{\labelitemi}{\raisebox{-2pt}{\Large \textbullet}} % Customize the first level bullet point character
\renewcommand{\labelitemii}{--} % Customize the second level bullet point character
\renewcommand{\labelitemiii}{$\circ$} % Customize the third level bullet point character


\newlist{checklist}{itemize}{2}
\setlist[checklist]{label=$\square$}

%----------------------------------------------------------------------------------------
%	LINKS
%----------------------------------------------------------------------------------------

\usepackage{hyperref} % Required for links
\hypersetup{
	colorlinks=true, 				% Whether to color links (a thin box is output around links if this is false)
	hidelinks, 							% Hide the default boxes around links
	urlcolor=Orchid, 				% Color for \url and \href links
	linkcolor=black, 				% Color for \ref/\nameref links
	citecolor=owaspdarkpurple, 	% Color for reference citations like \cite{}
	hyperindex=true, 				% Adds links from the page numbers in the index to the relevant page
	linktoc=all, 						% Link from section names and page numbers in the table of contents
}

%----------------------------------------------------------------------------------------
%	BOOKMARKS
%----------------------------------------------------------------------------------------

\usepackage{bookmark} % Required for customizing PDF bookmarks

\bookmarksetup{
	open, % Open all bookmark drawers automatically
	numbered, % Add section numbers to bookmarks
	addtohook={%
		\ifnum\bookmarkget{level}=-1 % Customize part bookmarks
			\bookmarksetup{color=owaspdarkpurple, bold}% Bold and colored
		\fi
		\ifnum\bookmarkget{level}=0 % Customize chapter bookmarks
			\bookmarksetup{bold}% Bold
		\fi
	}
}

%----------------------------------------------------------------------------------------
%	TITLE PAGE
%----------------------------------------------------------------------------------------

\renewcommand{\titlepage}[2]{
	\thispagestyle{empty} % Suppress headers and footers on the title page

	\begin{tikzpicture}[remember picture, overlay]
		\node [inner sep=0pt] at (current page.center) {#1}; % Background image
		\node [anchor=center, inner sep=1.25cm, rectangle, fill=owaspdarkpurple!30!white, fill opacity=0.6, text opacity=1, minimum height=0.2\paperheight, minimum width=\paperwidth, text width=0.8\paperwidth] at (current page.center) {#2}; % Title highlight box with title(s) and author(s)
	\end{tikzpicture}

	\newpage
}


%----------------------------------------------------------------------------------------
%	 LOAD PACKAGES THAT CLASH WITH OTHER PACKAGES
%----------------------------------------------------------------------------------------

\usepackage{tikz} % Required for drawing custom shapes and positioning elements absolutely on the page