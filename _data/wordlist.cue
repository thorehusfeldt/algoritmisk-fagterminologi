//  cue vet words.yml --schema words wordlist.cue

#Substantiv: {
	class: "substantiv"
	gender: "fælleskøn" | "intetkøn"
}
#Verbum: {
	class: "verbum"
}

#Construction: {
	title: string
	definition: string
	synonyms?: [...string]
}

#Entry: {
	title: string
	definition: string
	grammar?: #Substantiv | #Verbum
	declinations?: string
	etymology?: string
	english?: string
	synonyms?: [...string]
	near?: [...string]
	usage?: string
	example?: string
	constructions: [...#Construction]
}

words: [ ...#Entry]
