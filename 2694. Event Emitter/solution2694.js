class EventEmitter {
	eventsDict = {};
	id = 0;
	subscribe(event, cb) {
		if (!(event in this.eventsDict)) this.eventsDict[event] = [{ id: this.id, cb }];
		else this.eventsDict[event].push({ id: this.id, cb });
		this.id++;
		console.log(`eventsDict=${JSON.stringify(this.eventsDict)}`);
		return {
			unsubscribe: () => {
				const registeredCbs = this.eventsDict[event];
				console.log(`Unsuscribe id=${this.id-1}`);
				this.eventsDict[event] = registeredCbs.filter(elem => elem.id !== this.id - 1);
				console.log(`eventsDict=${JSON.stringify(this.eventsDict)}`);
			},
		};
	}

	emit(event, args = []) {
		if (!(event in this.eventsDict))
			return [];
		const retValues = [];
		for (let cb of this.eventsDict[event]) {
			retValues.push(cb.cb());
		}
		console.log(`retValues=${retValues}`);
		return retValues;
	}
}

const emitter = new EventEmitter();
// Subscribe to the onClick event with onClickCallback
function onClickCallback() {
	return 99;
}
const sub = emitter.subscribe('onClick', onClickCallback);

emitter.emit('onClick'); // [99]
sub.unsubscribe(); // undefined
emitter.emit('onClick'); // []

