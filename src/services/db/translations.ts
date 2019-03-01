import { database, CustomDb } from '../../config/mongodb'
import { schema } from '../../models/translation'
import * as translations from '../translations/locales'
import { DictionaryInterface } from '../translations/dictionary'
import { setTranslation } from '../translations'

export function saveTranslation(dictionary: DictionaryInterface) {
    return database.then((db: CustomDb) => (
        db.collection('translations').findOne({
            locale: { $eq: dictionary.locale }
        }).then((foundDictionary) => { updateTranslation({...dictionary, ...foundDictionary}) })
    ))
}

export function initTranslations() {
    return database.then((db: CustomDb) => (
        db.createCollection('translations', {
            validator: {
                $jsonSchema: schema
            }
        })
        .then(() => (
            Promise.all(Object.keys(translations).map(key => (
                saveTranslation((<any>translations)[key])
            )))
        ))
        .then(setTranslations)
    ))
}

export function updateTranslation(dictionary: DictionaryInterface) {
     return database.then((db: CustomDb) => (
        db.collection('translations').updateOne({
            locale: { $eq: dictionary.locale }
        }, {
            $set: dictionary
        }, {
            upsert: true
        })
    ))
}

function setTranslations() {
    return database.then((db: CustomDb) => (
        db.collection('translations').find({}).forEach(translation => {
            setTranslation(translation)
        })
    ))
}