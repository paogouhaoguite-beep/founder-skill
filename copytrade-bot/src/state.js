import fs from 'node:fs';

// Positions and history, saved to disk after every change so a restart picks
// up where it left off. Raw token amounts are stored as strings (BigInt-safe).
export class State {
  constructor(file) {
    this.file = file;
    this.data = { positions: {}, closed: [] };
    if (fs.existsSync(file)) this.data = { ...this.data, ...JSON.parse(fs.readFileSync(file, 'utf8')) };
  }

  save() {
    const tmp = `${this.file}.tmp`;
    fs.writeFileSync(tmp, JSON.stringify(this.data, null, 2));
    fs.renameSync(tmp, this.file);
  }

  get positions() { return this.data.positions; }
  get closed() { return this.data.closed; }
  openCount() { return Object.keys(this.data.positions).length; }
}
