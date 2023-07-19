import { db } from '../database';

export class PodcastHost {
  constructor(id, name, email) {
    if (!name || !email) {
      throw new Error('Invalid podcast host data');
    }
    this.id = id;
    this.name = name;
    this.email = email;
  }

  save() {
    return db.run(`INSERT INTO podcast_hosts (name, email) VALUES (?, ?)`, [this.name, this.email])
      .catch(err => {
        console.error('Error saving podcast host:', err);
        throw err;
      });
  }

  static delete(id) {
    return db.run(`DELETE FROM podcast_hosts WHERE id = ?`, [id])
      .catch(err => {
        console.error('Error deleting podcast host:', err);
        throw err;
      });
  }

  static update(id, name, email) {
    return db.run(`UPDATE podcast_hosts SET name = ?, email = ? WHERE id = ?`, [name, email, id])
      .catch(err => {
        console.error('Error updating podcast host:', err);
        throw err;
      });
  }

  static findAll() {
    return db.all(`SELECT * FROM podcast_hosts`)
      .catch(err => {
        console.error('Error finding podcast hosts:', err);
        throw err;
      });
  }

  static findById(id) {
    return db.get(`SELECT * FROM podcast_hosts WHERE id = ?`, [id])
      .catch(err => {
        console.error('Error finding podcast host:', err);
        throw err;
      });
  }
}